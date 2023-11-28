from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    # 投稿する写真のカテゴリを管理するモデル

    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    
    def __str__(self):
        # オブジェクトを文字列に変換して返す

        # Returns(str):カテゴリ名
        return self.title

class PhotoPost(models.Model):
    # 投稿されたデータを管理するモデル
    # CustomUserモデル（のuser_id)とPhotoPostモデルを
    # 1対多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        # ForeigKey =主キー的なもの
        CustomUser,
        verbose_name='ユーザー',
        # ユーザーを削除する場合は、そのユーザーの投稿データも全て削除する
        # on_delete= どこまで削除するか
        on_delete=models.CASCADE
        )

    # Categoryモデル（のtitle)とPhotoPostモデルを
    # 1対多の関係で結びつける
    # Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',    #フィールドのタイトル
        max_length=200             #最大文字200文字
        )
    # コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント',    #フィールドのタイトル
        )
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ１',  #フィールドのタイトル
        upload_to = 'photos'       #MEDIA_PORT以下のphotoにファイルを保存
        )    
    # イメージのフィールド２
    image2 = models.ImageField(
        verbose_name='イメージ２',  #フィールドのタイトル
        upload_to = 'photos',      #MEDIA_PORT以下のphotoにファイルを保存
        blank=True,                #フィールド値の設定は必須ではない
        null=True                   #データベースにnullが保存されることを許容
        )
        # イメージのフィールド3
    image3 = models.ImageField(
        verbose_name='イメージ3',  #フィールドのタイトル
        upload_to = 'photos',      #MEDIA_PORT以下のphotoにファイルを保存
        blank=True,                #フィールド値の設定は必須ではない
        null=True                   #データベースにnullが保存されることを許容
        )
        # イメージのフィールド4
    image2 = models.ImageField(
        verbose_name='イメージ4',  #フィールドのタイトル
        upload_to = 'photos',      #MEDIA_PORT以下のphotoにファイルを保存
        blank=True,                #フィールド値の設定は必須ではない
        null=True                   #データベースにnullが保存されることを許容
        )
    # イメージのフィールド5
    image2 = models.ImageField(
        verbose_name='イメージ5',  #フィールドのタイトル
        upload_to = 'photos',      #MEDIA_PORT以下のphotoにファイルを保存
        blank=True,                #フィールド値の設定は必須ではない
        null=True                   #データベースにnullが保存されることを許容
        )
    # イメージのフィールド6
    image2 = models.ImageField(
        verbose_name='イメージ6',  #フィールドのタイトル
        upload_to = 'photos',      #MEDIA_PORT以下のphotoにファイルを保存
        blank=True,                #フィールド値の設定は必須ではない
        null=True                   #データベースにnullが保存されることを許容
        )
    
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',     #フィールドのタイトル
        auto_now_add=True           #日時を自動追加
        )
    
    def __str__(self):
        # オブジェクトを文字列に変換して返す
        # Returns(str)：投稿記事のタイトル
        return self.title


class BlogPost(models.Model):
    #モデルクラス
    #カテゴリに設定する項目を入れ子のタプルとして定義
    #タプルの第一要素はモデルが使用する値、第二要素は管理サイトの選択メニューに表示する文字列
    CATEGORY = (('school','学校関連行事'),
                ('festival','お祭り'),
                ('ivent','イベント'),
                ('cleaning','清掃活動'),
                ('safety','安心・安全'),
                ('others','その他'))
    
    
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル',    #フィールドのタイトル
        max_length=200
        )
    #本文用のフィールド
    content = models.TextField(
        verbose_name='本文'
        )
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    #カテゴリーのフィールド
    category = models.CharField(
        verbose_name='カテゴリ', #フィールドのタイトル
        max_length=50,          #最大文字数は50
        choices=CATEGORY        #categoryフィールドにはCATEGORYの要素のみを登録
        )


    def __str__(self):
        #Django管理サイトでデータを表示する際に識別名として
        #投稿記事のタイトル（titleフィールドの値）を表示するために必要
        #Returns(str)：記事登校のタイトル
        return self.title