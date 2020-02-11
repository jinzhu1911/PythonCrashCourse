favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edeaid': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + '.')


# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())


# 使用当前键来访问与之相关联的值
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see you favorite language is " +
              favorite_languages[name].title() + "!")


# 遍历字典中的所有值
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# 使用集合set来提取不重复的列表
print("\nThe following languages have been mentioned without repeat:")
for language in set(favorite_languages.values()):
    print(language.title())


# 在字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
