import json

email_list = ['jvye@msn.com', 'vwxjjjg@msn.com', 'vhvxfuy@apple.com', 'yrhs@hotmail.com',
 'fsqqxo@apple.com', 'ulouyut@hotmail.com', 'focuwq@apple.com', 'jonl@msn.com',
'xjiwixj@msn.com', 'peej@yahoo.com', 'zjfsrsvv@gmail.com', 'leqoewm@hotmail.com',
'dkky@yahoo.com', 'tvqxjg@yahoo.com', 'lmmyz@hotmail.com', 'oclxjq@apple.com', 'qmfeff@yahoo.com',
 'hxuhnm@gmail.com', 'tyfjkw@hotmail.com', 'dpynrsq@apple.com', 'wyhyprqv@apple.com', 'lbeuoqv@msn.com',
 'vgvrtx@apple.com', 'mgypi@gmail.com', 'jzvpr@msn.com', 'peej@yahoo.com', 'rtwjsl@msn.com', 'tinwl@apple.com',
 'udwo@gmail.com', 'qmfeff@yahoo.com', 'xmkhuppo@hotmail.com', 'hinqs@apple.com', 'fkhr@gmail.com',
'dpynrsq@apple.com', 'qjjxjqi@yahoo.com', 'ykux@yahoo.com', 'hldqqhlj@apple.com', 'fnti@yahoo.com',
'rmmmr@apple.com', 'peej@yahoo.com', 'dpynrsq@apple.com', 'gvpzty@msn.com', 'gfngl@apple.com', 'qlxg@apple.com',
 'mmwfg@apple.com', 'bvsfzk@msn.com', 'cbwiojkj@gmail.com', 'bhlh@yahoo.com', 'gzxs@yahoo.com', 'kjpoojm@gmail.com',
'ndnyfvjo@msn.com', 'mhvingou@hotmail.com', 'brjf@apple.com', 'ejdltm@hotmail.com']

final_list = []
for x in email_list:
    if x not in final_list:
        final_list.append(x)
print(len(email_list))
print(len(final_list))

#-------------------------json--file-----------------

with open('clear_duplication.json', 'w') as email_file:
    json.dump(final_list, email_file)