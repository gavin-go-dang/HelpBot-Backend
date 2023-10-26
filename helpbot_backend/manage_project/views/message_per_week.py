from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Message


def get_date(pre_days):
    today = datetime.today()
    return today - timedelta(days=pre_days)


class MessageReceivedPerWeekAPI(APIView):
    def get(self, request):
        try:
            message_count = []
            date = []
            for day in range(0, 7):
                message_in_day_count = Message.objects.filter(created_at__date=get_date(day)).count()
                message_count.append(message_in_day_count)
                date.append(get_date(day).strftime("%Y-%m-%d"))
            return Response({"count": message_count[::-1], "date": date[::-1]}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
