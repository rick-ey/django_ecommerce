# /djangular_polls/serializers.py
from rest_framework import serializers
from djangular_polls.models import Poll, PollItem


class PollItemSerializer(serializers.ModelSerializer):
    percentage = serializers.ReadOnlyField()

    class Meta:
        model = PollItem
        fields = ('id', 'poll', 'name', 'text', 'votes', 'percentage')
        read_only_fields = ('id', 'poll', 'percentage')


class PollSerializer(serializers.ModelSerializer):
    items = PollItemSerializer(many=True, required=False)
    total_votes = serializers.ReadOnlyField()

    class Meta:
        model = Poll
        fields = ('id', 'title', 'publish_date', 'items', 'total_votes')
        read_only_fields = ('id', 'total_votes')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        poll = Poll.objects.create(**validated_data)
        for item_data in items_data:
            PollItem.objects.create(poll=poll, **item_data)
        return poll
