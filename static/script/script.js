document.addEventListener('DOMContentLoaded', () => {
    const shortenBtn = document.getElementById('shortenBtn');
    const longUrlInput = document.getElementById('longUrl');
    const resultDiv = document.getElementById('result');

    // Safety check (prevents JS errors if elements not found)
    if (!shortenBtn || !longUrlInput || !resultDiv) {
        console.error("Required HTML elements not found.");
        return;
    }

    shortenBtn.addEventListener('click', async (event) => {
        event.preventDefault(); // IMPORTANT: prevent form reload

        const longUrl = longUrlInput.value.trim();

        if (!longUrl) {
            alert("Please enter a valid URL!");
            return;
        }

        try {
            const response = await fetch('/shorten', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url: longUrl })
            });

            // Handle non-200 responses
            if (!response.ok) {
                throw new Error("Server error");
            }

            const data = await response.json();

            if (data.short_url) {
                resultDiv.innerHTML = `
                    <p><strong>Shortened URL:</strong></p>
                    <a href="${data.short_url}" target="_blank" rel="noopener noreferrer">
                        ${data.short_url}
                    </a>
                `;
            } else {
                resultDiv.textContent = "Failed to shorten URL. Try again!";
            }

        } catch (error) {
            console.error(error);
            resultDiv.textContent = "Error! Could not connect to server.";
        }
    });
});
