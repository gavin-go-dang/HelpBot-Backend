from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Message


def get_date(pre_months):
    today = datetime.today()
    return today - timedelta(days=pre_months * 30)


class MessageReceivedPerMonthAPI(APIView):
    def get(self, request):
        try:
            message_count = []
            date = []
            for month in range(0, 12):
                message_in_month_count = Message.objects.filter(
                    created_at__gte=get_date(month + 1), created_at__lt=get_date(month)
                ).count()
                message_count.append(message_in_month_count)
                date.append(get_date(month).strftime("%m/%y"))
            return Response({"count": message_count[::-1], "date": date[::-1]}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
