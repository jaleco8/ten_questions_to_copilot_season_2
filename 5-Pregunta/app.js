const axios = require('axios');

axios.get('https://jsonplaceholder.typicode.com/posts')
  .then(response => {
    const posts = response.data;
    posts.slice(0, 5).forEach(post => {
      console.log(post.title);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });