from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from .models import Ticket, Order

from cinema.models import Session, Seat, Pricing
from user.models import ClubCard

from .serializers import (
    TicketSerializer,
    ListTicketSerializer,
    OrderSerializer,
    CreateTicketSerializer,
    PayOrderSerializer,
)


class TicketView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_staff:
            return Ticket.objects.filter(user=user)
        return Ticket.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.user
        try:
            session = request.data['session']
            seats = request.data['seats']
        except KeyError:
            raise ValidationError({"Invalid data": request.data})

        if len(seats) > 6:
            raise ValidationError({
                'Tickets': 'Can book only 6 tickets for a session'
            })

        try:
            session = Session.objects.get(id=session)
        except Session.DoesNotExist:
            raise ValidationError({'Session': 'Session does not exist'})

        data = []

        for seat in seats:
            try:
                row = seat['row']
                column = seat['column']
                category = seat['category']
            except KeyError:
                raise ValidationError({
                    "Invalid data": seats
                })

            print(seat)

            try:
                st = Seat.objects.get(
                    row=row,
                    column=column,
                    room=session.room
                )
            except Seat.DoesNotExist:
                raise ValidationError({'Seat': 'Seat does not exist'})

            if Ticket.objects.filter(seat=st, session=session).exists():
                raise ValidationError({
                    'Seat': 'Seat is already booked for this session',
                    'Data': seat
                })

            data.append({
                'user': user.id,
                'session': session.id,
                'seat': st.id,
                'category': category
            })

        pricing = Pricing.objects.get(session=session)

        order = Order.objects.create(user=user)

        total_price = 0.0

        ret = {
            'Tickets': []
        }

        for record in data:
            record['order'] = order.id

            serializer = TicketSerializer(
                data=record,
                context={'request': request}
            )

            if serializer.is_valid():
                serializer.save(user=user, order=order)
                serializer.save()
                ret['Tickets'].append(serializer.data)
            else:
                raise ValidationError({
                    'Ticket': 'Invalid data',
                    'Data': record
                })

            if record['category'] == 1:
                total_price += pricing.children
            elif record['category'] == 2:
                total_price += pricing.student
            else:
                total_price += pricing.adult

        clubcard = ClubCard.objects.get(user=user)

        order.total_price = total_price - total_price * (clubcard.discount/100)
        order.save()

        return Response(ret, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTicketSerializer

        return ListTicketSerializer


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if not user.is_staff:
            return Order.objects.filter(user=user, paid=False)
        return Order.objects.filter(paid=False)


class PurchasesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    allowed_methods = ['GET', 'HEAD']

    def get_queryset(self):
        user = self.request.user

        if not user.is_staff:
            return Order.objects.filter(user=user, paid=True)
        return Order.objects.filter(paid=True)


class PayOrderView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PayOrderSerializer

    def create(self, request, *args, **kwargs):
        user = request.user

        try:
            order = request.data['order']
            payment_method = request.data['payment_method']
        except KeyError:
            raise ValidationError({"Invalid data": request.data})

        try:
            order = Order.objects.get(id=order)
        except Order.DoesNotExist:
            raise ValidationError({'Order': 'Order does not exist'})

        order.payment_method = payment_method
        order.paid = True
        order.save()

        clubcard = ClubCard.objects.get(user=user)
        clubcard.spent += order.total_price

        if clubcard.spent > 5000 and clubcard.discount < 40:
            if clubcard.discount == 0:
                clubcard.discount = 10
            elif clubcard.spent >= 10000:
                clubcard.discount += (clubcard.spent // 5000 - 1)

        clubcard.save()

        return Response({
            "Successful Payment": OrderSerializer(
                instance=order, context={'request': request}).data
        })
