import vk_api

login = 'телефон'
password = 'пароль'
group_id = -216477432 #айди группы
vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()

posts = vk.wall.get(count=100, access_token= '', owner_id=group_id)['items'] 
while(posts):                                        
    for post in posts:                             
        vk.wall.delete(owner_id=group_id, post_id=post['id'])
        print(str(post['id']) + ' пост успешно удален')         
    posts = vk.wall.get(count=100, owner_id=group_id)['items']
print('все посты группы удалены :)')