# Followers on Instagram
instagram_followers = {"Alice", "Bob", "Charlie", "David"}

# Followers on Twitter
twitter_followers = {"Charlie", "David", "Eve", "Frank"}

print("Instagram followers:", instagram_followers)
print("Twitter followers:", twitter_followers)

# 1. Followers on both platforms
print("\nFollowers on both platforms:")
both = instagram_followers & twitter_followers
print(both)

# 2. Followers exclusive to Instagram
print("Followers exclusive to Instagram:")
only_instagram = instagram_followers - twitter_followers
print(only_instagram)

# 3. Followers who follow at least one account
print("Followers who follow at least one account:")
at_least_one = instagram_followers | twitter_followers
print(at_least_one)

# Union of both sets
# All unique followers

# 4. Followers who don’t overlap between the two
print("Number of followers who don’t overlap:")
non_overlap = instagram_followers ^ twitter_followers
print(len(non_overlap))

# ^ → symmetric difference
# People in only one platform

#Overlap followers =
#people who follow both Instagram AND Twitter

# Non-overlapping followers
#These are people who are in only one platform, not both.