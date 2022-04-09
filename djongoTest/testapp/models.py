from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    u_name = models.TextField(null=True, default="홍길동")
    u_email = models.EmailField(default="aaaaa@aaa.com")

    class Meta:
        db_table = "user"