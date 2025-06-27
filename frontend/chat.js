document.getElementById('chat-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const message = document.getElementById('message').value;

  const res = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  });

  const data = await res.json();
  document.getElementById('response').innerText = data.response || data.error || 'No response.';
});
