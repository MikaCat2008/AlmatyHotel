function ShowText(text, type) {
    let ShowTextElement = document.querySelector("#show-text");

    ShowTextElement.querySelector("span").innerHTML = text;
    ShowTextElement.classList.add("show-text-out");

    if (type == 1) {
        ShowTextElement.classList.add("show-text-success");
    }
    else if (type == 2) {
        ShowTextElement.classList.add("show-text-error");
    }

    setTimeout(() => {
        ShowTextElement.classList.remove("show-text-out");

        if (type == 1) {
            ShowTextElement.classList.remove("show-text-success");
        }
        else if (type == 2) {
            ShowTextElement.classList.remove("show-text-error");
        }
    }, 2500);
}
