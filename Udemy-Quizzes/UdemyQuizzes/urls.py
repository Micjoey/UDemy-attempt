from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import quizzes.views
import quizzes.api_views

urlpatterns = [
    path('api/v1/questions/', quizzes.api_views.QuizzesList.as_view()),
    # path('api/v1/questions/new', quizzes.api_views.ProductCreate.as_view()),
    # path('api/v1/questions/<int:id>/',
    #      quizzes.api_views.ProductRetrieveUpdateDestroy.as_view()
    #      ),
    # path('api/v1/questions/<int:id>/stats',
    #      quizzes.api_views.questionstats.as_view(),
    #      ),

    path('admin/', admin.site.urls),
    path('questions/<int:id>/', quizzes.views.show, name='question'),
    path('', quizzes.views.index, name='list-questions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
