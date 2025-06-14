document.getElementById("employeeForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const position = document.getElementById("position").value;

    const table = document.getElementById("employeeTable").getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
    newRow.innerHTML = `<td>${name}</td><td>${email}</td><td>${position}</td>
                        <td><button onclick="deleteRow(this)">Delete</button></td>`;

    this.reset();
});

function deleteRow(btn) {
    btn.closest("tr").remove();
}
