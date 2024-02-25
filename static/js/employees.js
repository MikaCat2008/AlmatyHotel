let employees = {};


async function CreateEmployeePost(
    EmployeeFullName, EmployeeAge, EmployeeGender, EmployeeJob, 
    EmployeeSalary, EmployeePhone, EmployeeAddress, EmployeeMail
) {
    return await PostData("/create-employee", {
        employee: [
            EmployeeFullName, EmployeeAge, EmployeeGender, EmployeeJob, 
            EmployeeSalary, EmployeePhone, EmployeeAddress, EmployeeMail
        ]
    });
}


async function GetEmployeesPost() {
    return await PostData("/get-employees", {});
}


async function UpdateEmployeePost(
    EmployeeId, EmployeeFullName, EmployeeAge, EmployeeGender, EmployeeJob, 
    EmployeeSalary, EmployeePhone, EmployeeAddress, EmployeeMail
) {
    return await PostData("/update-employee", {
        employee: [
            EmployeeId, EmployeeFullName, EmployeeAge, EmployeeGender, EmployeeJob, 
            EmployeeSalary, EmployeePhone, EmployeeAddress, EmployeeMail
        ]
    });
}


async function DeleteEmployeePost(EmployeeId) {
    return await PostData("/delete-employee", {
        employee_id: EmployeeId
    });
}


function AddEmployee(
    EmployeeId, EmployeeFullName, EmployeeAge, EmployeeGender, EmployeeJob, 
    EmployeeSalary, EmployeePhone, EmployeeAddress, EmployeeMail
) {
    let tbody = document.querySelector("#employees-table > tbody");
    let rowElement = tbody.insertRow();
    
    let EmployeeIdElement = rowElement.insertCell();
    let EmployeeFullNameElement = rowElement.insertCell();
    let EmployeeAgeElement = rowElement.insertCell();
    let EmployeeGenderElement = rowElement.insertCell();
    let EmployeeJobElement = rowElement.insertCell();
    let EmployeeSalaryElement = rowElement.insertCell();
    let EmployeePhoneElement = rowElement.insertCell();
    let EmployeeAddressElement = rowElement.insertCell();
    let EmployeeMailElement = rowElement.insertCell();
    let DeleteElement = rowElement.insertCell();

    rowElement.id = `employee-${EmployeeId}`;

    EmployeeIdElement.innerHTML = `${EmployeeId}`;

    EmployeeFullNameElement.innerHTML = `<input type="text" value="${EmployeeFullName}" size="19">`;
    EmployeeFullNameElement.querySelector("input").onkeyup = InputKeyUp;

    EmployeeAgeElement.innerHTML = `<input type="text" value="${EmployeeAge}" size="1">`;
    EmployeeAgeElement.querySelector("input").onkeyup = InputKeyUpNumber;

    EmployeeGenderElement.innerHTML = `
        <select>
            <option value="0">Женщина</option>
            <option value="1">Мужчика</option>
        </select>
    `;
    EmployeeGenderElement.querySelector("select").value = EmployeeGender;
    EmployeeGenderElement.querySelector("select").onchange = SelectChange;

    EmployeeJobElement.innerHTML = `
        <select>
            <option value="0">Менеджер отеля (Hotel Manager)</option>
            <option value="1">Администратор (Front Desk Clerk)</option>
            <option value="2">Консьерж (Concierge)</option>
            <option value="3">Портье (Bellhop)</option>
            <option value="4">Горничная (Housekeeper)</option>
            <option value="5">Повар (Chef)</option>
            <option value="6">Повара-помощники (Cook)</option>
            <option value="7">Официанты (Waitstaff)</option>
            <option value="8">Технический персонал (Maintenance Staff)</option>
            <option value="9">Менеджер по продажам (Sales Manager)</option>
        </select>
    `;
    EmployeeJobElement.querySelector("select").value = EmployeeJob;
    EmployeeJobElement.querySelector("select").onchange = SelectChange;

    EmployeeSalaryElement.innerHTML = `<input type="text" value="${EmployeeSalary}" size="1">`;
    EmployeeSalaryElement.querySelector("input").onkeyup = InputKeyUpNumber;

    EmployeePhoneElement.innerHTML = `<input type="text" value="${EmployeePhone}" size="6">`;
    EmployeePhoneElement.querySelector("input").onkeyup = InputKeyUp;

    EmployeeAddressElement.innerHTML = `<input type="text" value="${EmployeeAddress}" size="7">`;
    EmployeeAddressElement.querySelector("input").onkeyup = InputKeyUp;

    EmployeeMailElement.innerHTML = `<input type="text" value="${EmployeeMail}" size="8">`;
    EmployeeMailElement.querySelector("input").onkeyup = InputKeyUp;

    DeleteElement.innerHTML = "X";
    DeleteElement.onclick = () => DeleteEmployee(EmployeeId);
    DeleteElement.classList.add("delete-element");

    employees[EmployeeId] = [
        EmployeeFullNameElement.querySelector("input"),
        EmployeeAgeElement.querySelector("input"),
        EmployeeGenderElement.querySelector("select"),
        EmployeeJobElement.querySelector("select"),
        EmployeeSalaryElement.querySelector("input"),
        EmployeePhoneElement.querySelector("input"),
        EmployeeAddressElement.querySelector("input"),
        EmployeeMailElement.querySelector("input")
    ]
}


async function CreateEmployee() {
    let EmployeeFullNameElement = document.querySelector("#employee-full-name > input");
    let EmployeeAgeElement = document.querySelector("#employee-age > input");
    let EmployeeGenderElement = document.querySelector("#employee-gender > select");
    let EmployeeJobElement = document.querySelector("#employee-job > select");
    let EmployeeSalaryElement = document.querySelector("#employee-salary > input");
    let EmployeePhoneElement = document.querySelector("#employee-phone > input");
    let EmployeeAddressElement = document.querySelector("#employee-address > input");
    let EmployeeMailElement = document.querySelector("#employee-mail > input");

    if (EmployeeFullNameElement.value == "") {
        return ShowText("Поле с ФИО не может быть пустым!", 2);
    }

    if (EmployeeAgeElement.value == "") {
        return ShowText("Поле с возрастом не может быть пустым!", 2);
    }

    if (EmployeeSalaryElement.value == "") {
        return ShowText("Поле с окладом не может быть пустым!", 2);
    }

    if (EmployeePhoneElement.value == "") {
        return ShowText("Поле с телефоном не может быть пустым!", 2);
    }

    if (EmployeeAddressElement.value == "") {
        return ShowText("Поле с адресом не может быть пустым!", 2);
    }

    if (EmployeeMailElement.value == "") {
        return ShowText("Поле с почтой не может быть пустым!", 2);
    }

    if (isNaN(Number(EmployeeAgeElement.value))) {
        return ShowText("Возраст должен быть числом!", 2);
    }

    if (isNaN(Number(EmployeeSalaryElement.value))) {
        return ShowText("Оклад должен быть числом!", 2);
    }

    await CreateEmployeePost(
        EmployeeFullNameElement.value,
        EmployeeAgeElement.value,
        EmployeeGenderElement.value,
        EmployeeJobElement.value,
        EmployeeSalaryElement.value,
        EmployeePhoneElement.value,
        EmployeeAddressElement.value,
        EmployeeMailElement.value,
    ).then(data => {
        if (data.status) {
            return ShowText("Сотрудник успешно добавлен!", 1);
        }
    });;
}


function GetEmployee(element) {
    let tr = element.parentElement.parentElement;
    
    let EmployeeId = Number(tr.id.split("-")[1]);
    let employee = employees[EmployeeId]
    let EmployeeFullName = employee[0].value;
    let EmployeeAge = Number(employee[1].value);
    let EmployeeGender = Boolean(employee[2].value);
    let EmployeeJob = Number(employee[3].value);
    let EmployeeSalary = Number(employee[4].value);
    let EmployeePhone = employee[5].value;
    let EmployeeAddress = employee[6].value;
    let EmployeeMail = employee[7].value;

    return [
        EmployeeId, EmployeeFullName, EmployeeAge, EmployeeGender, EmployeeJob, 
        EmployeeSalary, EmployeePhone, EmployeeAddress, EmployeeMail
    ];
}


function SelectChange(event) {
    let element = event.target;

    UpdateEmployeePost(...GetEmployee(element)).then(response => {
        if (response.status) {
            SetChange(element);
        }
    });
}


function InputKeyUp(event) {
    if (event.key == "Enter") {
        let element = event.target;

        UpdateEmployeePost(...GetEmployee(element)).then(data => {
            if (data.status) {
                SetChange(element);
            }
        });
    }
}


function InputKeyUpNumber(event) {
    if (event.key == "Enter") {
        let element = event.target;
        
        let number = Number(element.value);

        if (isNaN(number)) {
            SetError(element);
        }
        else {
            UpdateEmployeePost(...GetEmployee(element)).then(data => {
                if (data.status) {
                    SetChange(element);
                }
            });
        }
    }
}


function DeleteEmployee(EmployeeId) {
    let employee = employees[EmployeeId];

    DeleteEmployeePost(EmployeeId).then(data => {
        if (data.status) {
            for (let i = 0; i < 8; i++) {
                const element = employee[i];

                SetError(element);
            }
        }
    });
}


async function LoadEmployees() {
    StartLoadingAnimation();

    GetEmployeesPost().then(data => {
        StopLoadingAnimation();

        data.employees.forEach(room => {
            AddEmployee(...room);
        });
    });
}