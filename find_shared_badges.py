fs_shared_badges = file('/Users/liz/Dropbox/Bitly/Code/FS_data/fs_shared_badges.csv', 'w')

f1 = set(open('fs_badges.csv').readlines())
f2 = set(open('fs_badges2.csv').readlines())

similarities = f1 & f2 

fs_shared_badges.write('\n'.join(similarities))

fs_shared_badges.close()
