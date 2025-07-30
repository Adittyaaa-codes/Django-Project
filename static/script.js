function toggleLike(btn) {
    const icon = btn.querySelector('i');
    const postId = btn.getAttribute('data-post-id');

    fetch('/like/', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `post_id=${postId}`
    })
    .then(response => response.json())
    .then(data => {
        icon.classList.toggle('bi-heart-fill', data.liked);
        icon.classList.toggle('bi-heart', !data.liked);
        icon.classList.toggle('text-danger', data.liked);

        const likeCount = btn.nextElementSibling;
        if (likeCount) {
            likeCount.textContent = data.likes;
        }
    });
}
