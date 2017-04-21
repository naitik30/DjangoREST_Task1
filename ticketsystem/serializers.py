from rest_framework import serializers
from .models import ticket

class ticketSerializer(serializers.ModelSerializer):

    class Meta:
        model = ticket
        fields = ('rider_num')
    def crate(self,data):
        # print(ticket.objects.all().count())
        if ticket.objects.all().count() + int(data['seats'])<=10:
            rider_list=[int(i) for i  in data['rider_id' ].strip('}').strip('{').split(',')]
            for i in rider_list:
                ticket_data = ticket(rider_num = i)
                ticket_data.save()
            return True
        else:
            return False

    def drop(self,data):
        rider_list=[int(i) for i  in data['rider_id' ].strip('}').strip('{').split(',')]
        for i in rider_list:
            try:
                rider = ticket.objects.get(rider_num = i)
            except rider.DoesNotExist:
                return Response("rider not exist"+str(i))
            rider.delete()

        return "total fare  = "+str(2*len(rider_list))+"$"
