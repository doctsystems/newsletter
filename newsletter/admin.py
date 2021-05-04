# from django.contrib import admin
# from .models import *
# # Register your models here.

# admin.site.register(Newsletter)
# admin.site.register(Subscriber)
# admin.site.register(Issue)
# admin.site.register(Subscription)

from django.contrib import admin

from .tasks import send_issue
from .models import Newsletter, Subscriber, Issue, Subscription

admin.site.register(Subscription)


def send(modeladmin, request, queryset):
  for issue in queryset:
    send_issue.delay(issue.id)


send.short_description = "send"


class IssueInline(admin.StackedInline):
  model = Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
  actions = [send]


class SubscriptionAdmin(admin.StackedInline):
  model = Subscription
  pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
  inlines = (IssueInline, SubscriptionAdmin)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
  inlines = (SubscriptionAdmin,)

