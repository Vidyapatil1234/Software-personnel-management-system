document.addEventListener("DOMContentLoaded", function() {
    console.log("Total Employees Page Loaded");
});

// Open Promotion Form
function openPromotionForm(employeeId, employeeName) {
    document.getElementById("employee_id").value = employeeId;
    document.getElementById("promotionModal").style.display = "block";
}

// Close Promotion Form
function closePromotionForm() {
    document.getElementById("promotionModal").style.display = "none";
}

// Confirm Before Deleting Employee
document.querySelectorAll(".delete-btn").forEach(button => {
    button.addEventListener("click", function(event) {
        if (!confirm("Are you sure you want to remove this employee?")) {
            event.preventDefault(); // Stop form submission
        }
    });
});
