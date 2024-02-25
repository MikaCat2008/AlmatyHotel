function SetError(element) {
    element.classList.add("error-element");
    element.parentElement.classList.add("error-parent-element");
    
    if (element.classList.contains("change-element")) {
        element.classList.remove("change-element");
        element.parentElement.classList.remove("change-parent-element");
    }
}


function SetChange(element) {
    element.classList.add("change-element");
    element.parentElement.classList.add("change-parent-element");
    
    if (element.classList.contains("error-element")) {
        element.classList.remove("error-element");
        element.parentElement.classList.remove("error-parent-element");
    }
}
