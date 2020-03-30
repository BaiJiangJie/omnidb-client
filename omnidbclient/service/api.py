
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterDatabaseConnection(APIView):

    def post(self, request, *args, **kwargs):
        # 获取数据
        user_id = request.POST.get('user_id')
        database_app_id = request.POST.get('database_app_id')
        system_user_id = request.POST.get('system_user_id')
        # 校验用户权限
        # 校验用户数据库权限
        # 获取数据库应用信息
        # 注册数据库应用连接
        # 返回数据库连接url
        return Response(data={'url': 'http://localhost:8000/workspace/'}, status=200)

    def get(self, request, *args, **kwargs):
        return Response(data={'url': 'http://localhost:8000/workspace/'}, status=200)

