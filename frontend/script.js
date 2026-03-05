async function analyzeText() {

    const text = document.getElementById("textInput").value;

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();

    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = `
        <p><b>Word count:</b> ${data.word_count}</p>
        <p><b>Characters (with spaces):</b> ${data.char_count_with_spaces}</p>
        <p><b>Characters (without spaces):</b> ${data.char_count_without_spaces}</p>
        <p><b>Sentence count:</b> ${data.sentence_count}</p>

        <h3>Top words</h3>
        <ul>
            ${data.top_words.map(w => `<li>${w.word}: ${w.count}</li>`).join("")}
        </ul>
    `;
}