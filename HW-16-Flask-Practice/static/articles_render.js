fetch('/api/articles')
    .then(response => response.json())
    .then(function (response) {
        var articles = document.getElementById('articles');
        response.forEach(function (article) {
            var card = document.createElement('div');
            card.classList.add('card');
            card.style.width = '18rem';

            var cardBody = document.createElement('div');
            cardBody.classList.add('card-body');

            var title = document.createElement('h5');
            title.classList.add('card-title');
            title.textContent = article.title;

            var subtitle = document.createElement('h6');
            subtitle.classList.add('card-subtitle', 'mb-2', 'text-body-secondary');
            subtitle.textContent = article.created_at;

            var body = document.createElement('p');
            body.classList.add('card-text');
            body.textContent = article.body;

            cardBody.appendChild(title);
            cardBody.appendChild(subtitle);
            cardBody.appendChild(body);
            
            if (article.user_id == article.user.id){
                const deleteLink = document.createElement('a');
                deleteLink.classList.add('card-link');
                deleteLink.textContent = 'Delete';
                deleteLink.href = `/article/${article.id}/delete`;
                cardBody.appendChild(deleteLink);
            }

            card.appendChild(cardBody);
            articles.appendChild(card);
        });
    })