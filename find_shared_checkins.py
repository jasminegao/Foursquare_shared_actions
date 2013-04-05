fs_shared_checkins = file('/Users/liz/Dropbox/Bitly/Code/FS_data/fs_shared_checkins.csv', 'w')

f1 = set(open('fs_checkins.csv').readlines())
f2 = set(open('fs_checkins2.csv').readlines())

similarities = f1 & f2 

fs_shared_checkins.write('\n'.join(similarities))

fs_shared_checkins.close()
