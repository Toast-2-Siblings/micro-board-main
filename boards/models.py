from django.db import models

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)                             # 게시판 ID (자동 증가)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE) # 사용자 ID (ForeignKey)
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # 게시판 생성일
    updated_at = models.DateTimeField(auto_now=True)        # 게시판 수정일
    is_deleted = models.BooleanField(default=False)         # 삭제 여부

    class Meta:
        db_table = 'boards'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Board{{\n"
            f"\tid='{self.id}',\n"
            f"\tuser_id='{self.user_id}',\n"
            f"\ttitle='{self.title}',\n"
            f"\tcontent='{self.content}',\n"
            f"\tcreated_at='{self.created_at}',\n"
            f"\tupdated_at='{self.updated_at}',\n"
            f"\tis_deleted='{self.is_deleted}',\n"
            f"}}"
        )