from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'kouka2app'

#URLパターンを登録するためのリスト
urlpatterns = [
    #http(s)//ホスト名/以下パスが''無しの場合
    #viwsモジュールのIndexviweを実行
    #URLパターン名は’Index’
    path('',views.IndexView.as_view(), name='index'),

        # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),

    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    
    # カテゴリ一覧ページ
    # photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category:id(int)}としてcategoryViewに渡される
        path('photos/<int:category>',
          views.CategoryView.as_view(),
          name = 'photos_cat'
          ),

    # ユーザー投稿の一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user:id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>',views.UserView.as_view(),
         name = 'user_list'
         ),

    # 詳細ページ
    # photos/<PhotoPostテーブルのid値>にマッチング
    # <int:pk>は辞書{pk:id値(int)}としてDetailViewに渡される
    path('photo-detail/<int:pk>',views.DetailView.as_view(),
         name = 'photo_detail'
         ),

    # マイページ
    # mypage/へのアクセスはMypaggeViewを実行
    path('mypage/',views.MypageView.as_view(),
         name = 'mypage'
         ),
    
    # 投稿写真の削除
    # photo/<photo postテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk:id値(int)}としてDetailViewに渡される
    path('photo/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(),
         name = 'photo_delete'
         ),

     # photogalleryトップ
    path('photogallery/',
         views.PhotogalleryView.as_view(),
         name = 'photogallery'
         ),


    #リクエストされたURLが「blob_detail1/レコードid/」の場合
    #viewモジュールのBlogDetailを実行
    #URLパターン名は'Blog_detail'
    path(
        #詳細ページのURLは｢blog-detail/レコードのid/」
        'blog-detail/<int:pk>/',
        #viewモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        #URLパターンの名前を'blog_detail'にする
        name='blog_detail'
        ),
    #festivalカテゴリーの一覧ページのURLパターン
    path(
        #festivalカテゴリーの一覧ページのURL｢festival-list｣
        'festival-list/',
        #viewsモジュールのBlogDetailを実行
        views.FestivalView.as_view(),
        #URLパターンの名前を'science_list'にする
        name='festival_list'
        ),
    #schoolカテゴリーの一覧ページのURLパターン
    path(
        #schoolカテゴリーの一覧ページのURL｢school-list｣
        'school-list/',
        #viewsモジュールのSchoolViewを実行
        views.SchoolView.as_view(),
        #URLパターンの名前を'school_list'にする
        name='school_list'
        ),
    #iventカテゴリーの一覧ページのURLパターン
    path(
        #iventカテゴリーの一覧ページのURL｢ivent-list｣
        '-list/',
        #viewsモジュールのIventViewを実行
        views.IventView.as_view(),
        #URLパターンの名前を'ivent_list'にする
        name='ivent_list'
        ),  

    #cleaningカテゴリーの一覧ページのURLパターン
    path(
        #cleaningカテゴリーの一覧ページのURL｢cleaning-list｣
        'cleaning-list/',
        #viewsモジュールのMusicViewを実行
        views.CleaningView.as_view(),
        #URLパターンの名前を'cleaning_list'にする
        name='cleaning_list'
        ),  

     #safetyカテゴリーの一覧ページのURLパターン
    path(
        #safetyカテゴリーの一覧ページのURL｢safety-list｣
        'safety-list/',
        #viewsモジュールのSafetyViewを実行
        views.SafetyView.as_view(),
        #URLパターンの名前を'safety_list'にする
        name='safety_list'
        ),  

    #othersカテゴリーの一覧ページのURLパターン
    path(
        #othersカテゴリーの一覧ページのURL｢others-list｣
        'others-list/',
        #viewsモジュールのOthersViewを実行
        views.OthersView.as_view(),
        #URLパターンの名前を'others_list'にする
        name='others_list'
        ),  


]

