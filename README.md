Blogging platform test task
===========

Create Django-backend (simple html is enough) with features:

1. Default Django user model with authentication (no registration needed).

2. Every user has own single blog.

3. Blog post - simple post with title, text and post date.

4. User can subscribe (unsubscribe) to other users blogs.

5. User has own newsfeed with posts from blogs which he subscribed.

6. User can mark posts as read.

7. Newsfeed changes when user subscribes or unsubscribes (no need to save read marks)

8. Subscribers should receive email notification when new post added at subscribed blogs.

9. Newsfeed updates and email notifications should work with post publishing via website and via admin interface.


Платформа для блогов - тестовое задание на Django
===========

Реализовать на Django бэкенд с минимальным фронтендом (можно на голом HTML) со следующей функциональностью:

1. Имеется база стандартных пользователей Django (добавляются через админку, регистрацию делать не надо).

2. У каждого пользователя есть персональный блог. Новые создавать он не может.

3. Пост в блоге — элементарная запись с заголовком, текстом и временем создания.

4. Пользователь может подписываться (отписываться) на блоги других пользователей (любое количество).

5. У пользователя есть персональная лента новостей, в которой в обратном хронологическом порядке выводятся посты из блогов, на которые он подписан.

6. Пользователь может помечать посты в ленте прочитанными.

7. При добавлении/удаление подписки содержание ленты меняется (при удалении подписки пометки о прочтении сохранять не нужно).

8. При добавлении поста в ленту — подписчики получают почтовое уведомление со ссылкой на новый пост.

9. Изменение содержания лент подписчиков (и рассылка уведомлений) должно происходить как при стандартной публикации поста пользователем через интерфейс сайта, так при добавлении/удалении поста через админку.
