from TikTokApi import TikTokApi
import time
import os

api = TikTokApi()


def getLikeCount():
    tiktoks = api.byUsername('jayspranks', count=1)
    for tiktok in tiktoks:
        likeCount = tiktok["stats"]["diggcount"]
        shareCount = tiktok["stats"]["sharecount"]
        commentCount = tiktok["stats"]["commentCount"]
        followCount = tiktok["authorStats"]["followerCount"]
        return (likeCount, shareCount, commentCount, followCount)


def bruh():
    print('bruh!')


def update():
    initLikeCount = 0
    initShareCount = 0
    initCommentCount = 0
    initFollowCount = 0

    while True:
        results = getLikeCount
        currentNumShares = results[1]
        print("sleepy time")
        time.sleep(5)

        if currentNumShares > initShareCount:
            newShares = currentNumShares - initShareCount
            initShareCount = currentNumShares
            print('amount of new shares = ', newShares)
            for x in range(newShares):
                bruh()

        else:
            print("No new shares")


update()

