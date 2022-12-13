from rest_framework import viewsets, status
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from .models import Ticket, Order

from cinema.models import Session, Room, Seat, Pricing

from .serializers import TicketSerializer, OrderSerializer, CreateTicketSerializer

class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_admin:
            return Ticket.objects.filter(user=user)
        return Ticket.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.user
        try:
            session = request.data['session']
            seats = request.data['seats']
        except:
            raise ValidationError({"Invalid data": request.data})

        if len(seats) > 6:
            raise ValidationError({'Tickets': 'Can book only 6 tickets for a session'})

        try :
            session = Session.objects.get(id=session)
        except Session.DoesNotExist:
            raise ValidationError({'Session': 'Session does not exist'})

        data = []

        for seat in seats:
            try:
                row = seat['row']
                column = seat['column']
                category = seat['category'] 
            except:
                raise ValidationError({"Invalid data": seats})

            print(seat)

            try:
                st = Seat.objects.get(row=row, column=column, room=session.room)
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

        ret = {
            'Tickets': []
        }

        for record in data:
            record['order'] = order.id

            serializer = TicketSerializer(data=record, context={'request': request})

            if serializer.is_valid():
                serializer.save(user=user, order=order)
                serializer.save()
                ret['Tickets'].append(serializer.data)
            else:
                raise ValidationError({
                    'Ticket': 'Invalid data',
                    'Data': record
                })

        return Response(ret, status=status.HTTP_201_CREATED)


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTicketSerializer
        
        return TicketSerializer


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_admin:
            return Order.objects.filter(user=user)
        return Order.objects.all()
