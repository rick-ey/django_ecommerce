# main/views.py

from django.shortcuts import render_to_response, RequestContext
from payments.models import User
from main.models import StatusReport
# from main.models import MarketingItem
# from main.templatetags.main_marketing import marketing__circle_item


class market_item(object):

    def __init__(self, img, heading, caption, button_link="register",
                 button_title="View details"):
        self.img = img
        self.heading = heading
        self.caption = caption
        self.button_link = button_link
        self.button_title = button_title


market_items = [
    market_item(
        img="yoda.jpg",
        heading="Hone your Jedi Skills",
        caption="All members have access to our unique"
        " training and achievements latters. Progress through the "
        "levels and show everyone who the top Jedi Master is!",
        button_title="Sign Up Now"
    ),
    market_item(
        img="clone_army.jpg",
        heading="Build your Clan",
        caption="Engage in meaningful conversation, or "
        "bloodthirsty battle! If it's related to "
        "Star Wars, in any way, you better believe we do it.",
        button_title="Sign Up Now"
    ),
    market_item(
        img="leia.jpg",
        heading="Find Love",
        caption="Everybody knows Star Wars fans are the "
        "best mates for Star Wars fans. Find your "
        "Princess Leia or Han Solo and explore the "
        "stars together.",
        button_title="Sign Up Now"
    ),
]


def index(request):
    uid = request.session.get('user')
    # market_items = MarketingItem.objects.all()
    if uid is None:
        # main landing page
        return render_to_response(
            'main/index.html',
            {'marketing_items': market_items}
        )
    else:
        # membership page
        status = StatusReport.objects.all().order_by('-when')[:20]
        return render_to_response(
            'main/user.html',
            {'user': User.get_by_id(uid), 'reports': status},
            context_instance=RequestContext(request),
        )


def report(request):
    if request.method == "POST":
        status = request.POST.get("status", "")

        # update the database with the status
        if status:
            uid = request.session.get('user')
            user = User.get_by_id(uid)
            StatusReport(user=user, status=status).save()

        # always return something
        return index(request)
