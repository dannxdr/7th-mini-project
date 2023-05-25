const form = document.querySelector(".question__form");
const textarea = document.querySelector(".question__textarea");
const questionBtn = document.querySelector(".question__btn");

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

const handleSubmit = async (event) => {
    event.preventDefault();

    const csrftoken = getCookie('csrftoken'); 
    const question = textarea.value;
    const type = document.querySelector("input[name=question_type]:checked").value;

    if (question.length === 0) {
        return;
    }

    const myChatWrapper = document.createElement("div");
    myChatWrapper.classList.add("chat__wrapper");
    const mySizedBox = document.createElement("div");
    mySizedBox.classList.add("speech-bubble__sizedbox"); 
    const mySpeechBubble= document.createElement("div");
    mySpeechBubble.classList.add("speech-bubble");
    mySpeechBubble.classList.add("speech-bubble--user");
    const mySpeechBubbleText = document.createElement("p");
    mySpeechBubbleText.classList.add("speech-bubble__text");
    mySpeechBubbleText.innerText = question;

    myChatWrapper.appendChild(mySpeechBubble);
    myChatWrapper.appendChild(mySizedBox);
    mySpeechBubble.appendChild(mySpeechBubbleText);
    form.insertAdjacentElement("beforebegin", myChatWrapper);

    textarea.value = "제출중... 잠시만 기다려주세요!";
    textarea.disabled = true;
    questionBtn.disabled = true;

    const response = await fetch("/selfchatgpt/chat/", {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "X-CSRFToken":csrftoken
            },
        body: JSON.stringify({input_text: question, question_type: type}),
        },
    );
    data = await response.json();

    const chatWrapper = document.createElement("div");
    chatWrapper.classList.add("chat__wrapper");
    const gptIcon = document.createElement("img");
    gptIcon.classList.add("chat__profile-img");
    gptIcon.src = "/static/images/chatgpt-icon.png";

    chatWrapper.appendChild(gptIcon);

    const speechBubble = document.createElement("div");
    speechBubble.classList.add("speech-bubble");

    if (type === "text") {
        speechBubble.classList.add("speech-bubble--gpt");
        const speechBubbleContent = document.createElement("p");
        speechBubbleContent.classList.add("speech-bubble__text");
        speechBubbleContent.innerText = data.result;
        chatWrapper.appendChild(speechBubble);
        speechBubble.appendChild(speechBubbleContent);
    } else {
        speechBubble.classList.add("speech-bubble--image");
        const speechBubbleContent = document.createElement("img");
        speechBubbleContent.classList.add("speech-bubble__image");
        speechBubbleContent.src = data.result;
        chatWrapper.appendChild(speechBubble);
        speechBubble.appendChild(speechBubbleContent);
    }

    form.insertAdjacentElement("beforebegin", chatWrapper);
    textarea.value = "";
    textarea.disabled = false;
    questionBtn.disabled = true;

}

const handleInput = (event) => {
    if (event.keyCode == 13) {
        event.preventDefault();
        questionBtn.click();
        return;
    }

    textarea.style.height = "1px";
    textarea.style.height = textarea.scrollHeight + "px";

    if (textarea.value.length > 0) {
        questionBtn.disabled = false;
    } else {
        questionBtn.disabled = true;
    }
}

textarea.addEventListener("keyup", handleInput);
form.addEventListener("submit", handleSubmit);