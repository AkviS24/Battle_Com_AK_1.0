from .models import Promotion, Rank


def get_current_rank(profile):
    return profile.current_rank


def get_next_rank(profile):
    return Rank.objects.filter(
        order__gt=profile.current_rank.order
    ).order_by('order').first()


def has_required_xp(profile, rank):
    return profile.xp >= rank.min_xp


def is_promotion_available(profile):
    next_rank = get_next_rank(profile)

    if next_rank is None:
        return False

    return has_required_xp(profile, next_rank)


def promote_automatically(profile):
    next_rank = get_next_rank(profile)

    while next_rank and not next_rank.requires_approval:
        if not has_required_xp(profile, next_rank):
            break

        profile.current_rank = next_rank
        profile.save(update_fields=['current_rank'])
        next_rank = get_next_rank(profile)

    return profile.current_rank



def approve_promotion(profile, approved_by):
    next_rank = get_next_rank(profile)

    if next_rank is None:
        return None

    if not has_required_xp(profile, next_rank):
        return None

    if not next_rank.requires_approval:
        return None

    if approved_by.profile.current_rank.abbreviation != "SMA":
        return None

    promotion = Promotion.objects.create(
        player=profile.user,
        from_rank=profile.current_rank,
        to_rank=next_rank,
        approved_by=approved_by,
    )

    profile.current_rank = next_rank
    profile.save(update_fields=['current_rank'])

    return promotion