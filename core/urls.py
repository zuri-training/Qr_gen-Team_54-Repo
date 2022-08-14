from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path("admin/", admin.site.urls),

    # site features
    path("", views.site_home, name="home_page"),
    path('faq/', views.faq, name="faq"),
    path('draft/', views.site_draft, name="draft"),
    path('terms/', views.site_terms, name="terms"),
    path('about/', views.about_us, name="about_us"),
    path('history/', views.site_history, name="history"),
    path('feedback/', views.site_feedback, name="feedback"),

    # encoding option url
    path('qrcode-options/', views.qr_code_options, name="qrcode_options"),

    # apps paths
    path("banks/", include("apps.banks.urls")),
    path("business/", include("apps.business.urls")),
    path("contact/", include("apps.contacts.urls")),
    path("image/", include("apps.images.urls")),
    path("music/", include("apps.music.urls")),
    path("pdf/", include("apps.pdfs.urls")),
    path("social/", include("apps.socials.urls")),
    path("text/", include("apps.texts.urls")),
    path("users/", include("apps.users.urls")),
    path("video/", include("apps.videos.urls")),
    path("website/", include("apps.websites.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
