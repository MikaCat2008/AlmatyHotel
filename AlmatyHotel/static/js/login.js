async function LoginPost(user, password) {
    return await PostData("/login", {
        user: user,
        password: password
    });
}


async function Login() {
    let UserElement = document.querySelector("#user > input");
    let PasswordElement = document.querySelector("#password > input");

    await LoginPost(
        UserElement.value,
        PasswordElement.value
    ).then(data => {
        if (data.status) {
            OpenAdminPanel();
        }
        else {
            ShowText("Неправильный логин или пароль!", 2);
        }
    });;
}


function OpenAdminPanel() {
    document.location.href = "/?just_logged=1";
}
