from djongo import models


class User(models.Model):
    u_id = models.TextField(primary_key=True, default="")
    u_name = models.TextField(default="홍길동")
    u_email = models.EmailField(unique=True, default="aaaaa@aaa.com")
    u_active_token = models.TextField(default="")
    u_warn_count=models.IntegerField(default=0)
    u_active = models.IntegerField(null=False, default=0)
    inactivated_date = models.DateField(null=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return ""+self.u_name+", "+self.u_email


class Manager(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column="u_id")
    m_tel = models.TextField(default="010-0101-1010")
    u_name = models.TextField()
    class Meta:
        db_table = "manager"
