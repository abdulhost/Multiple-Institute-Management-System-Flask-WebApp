const demoData = {
    superadmin: {
        institutes: [
            { id: 1, name: "Horizon Academy", location: "New York", students: 2000 },
            { id: 2, name: "Starlight Schools", location: "London", students: 1500 },
            { id: 3, name: "Global Education", location: "Sydney", students: 2500 },
            { id: 4, name: "Bright Future", location: "Toronto", students: 1800 },
            { id: 5, name: "Elite Institute", location: "Mumbai", students: 2200 }
        ],
        users: [
            { id: 1, name: "Sarah Patel", role: "Admin", institute: "Horizon Academy" },
            { id: 2, name: "James Lee", role: "Teacher", institute: "Starlight Schools" },
            { id: 3, name: "Aisha Khan", role: "Admin", institute: "Global Education" },
            { id: 4, name: "Michael Brown", role: "Student", institute: "Bright Future" },
            { id: 5, name: "Emma Wilson", role: "Parent", institute: "Elite Institute" }
        ],
        analytics: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            data: [500, 600, 700, 650, 800, 900]
        }
    },
    admin: {
        classes: [
            { id: 1, name: "Grade 10A", teacher: "John Doe", students: 30 },
            { id: 2, name: "Grade 10B", teacher: "Jane Smith", students: 28 },
            { id: 3, name: "Grade 11A", teacher: "Emily Davis", students: 25 },
            { id: 4, name: "Grade 11B", teacher: "Robert Wilson", students: 27 },
            { id: 5, name: "Grade 12A", teacher: "Sarah Patel", students: 29 }
        ],
        fees: [
            { id: 1, student: "Alice Johnson", amount: 1000, status: "Paid", date: "2025-06-01" },
            { id: 2, student: "Bob Smith", amount: 1200, status: "Pending", date: "2025-06-05" },
            { id: 3, student: "Charlie Brown", amount: 1000, status: "Paid", date: "2025-06-03" },
            { id: 4, student: "Diana Lee", amount: 1100, status: "Pending", date: "2025-06-07" },
            { id: 5, student: "Emma Wilson", amount: 1000, status: "Paid", date: "2025-06-02" }
        ],
        attendance: [
            { id: 1, student: "Alice Johnson", date: "2025-06-10", status: "Present" },
            { id: 2, student: "Bob Smith", date: "2025-06-10", status: "Absent" },
            { id: 3, student: "Charlie Brown", date: "2025-06-10", status: "Present" },
            { id: 4, student: "Diana Lee", date: "2025-06-10", status: "Present" },
            { id: 5, student: "Emma Wilson", date: "2025-06-10", status: "Absent" }
        ],
        analytics: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            data: [95, 92, 90, 93, 94, 96]
        }
    },
    teacher: {
        schedule: [
            { id: 1, day: "Monday", time: "09:00-10:00", class: "Grade 10A", subject: "Math" },
            { id: 2, day: "Monday", time: "10:00-11:00", class: "Grade 10B", subject: "Science" },
            { id: 3, day: "Tuesday", time: "09:00-10:00", class: "Grade 11A", subject: "Math" },
            { id: 4, day: "Tuesday", time: "10:00-11:00", class: "Grade 11B", subject: "Science" },
            { id: 5, day: "Wednesday", time: "09:00-10:00", class: "Grade 12A", subject: "Math" }
        ],
        attendance: [
            { id: 1, student: "Alice Johnson", date: "2025-06-10", status: "Present", class: "Grade 10A" },
            { id: 2, student: "Bob Smith", date: "2025-06-10", status: "Absent", class: "Grade 10A" },
            { id: 3, student: "Charlie Brown", date: "2025-06-10", status: "Present", class: "Grade 10B" },
            { id: 4, student: "Diana Lee", date: "2025-06-10", status: "Present", class: "Grade 10B" },
            { id: 5, student: "Emma Wilson", date: "2025-06-10", status: "Absent", class: "Grade 11A" }
        ],
        exams: [
            { id: 1, name: "Midterm", date: "2025-07-01", class: "Grade 10A", status: "Scheduled" },
            { id: 2, name: "Final", date: "2025-12-01", class: "Grade 10B", status: "Scheduled" },
            { id: 3, name: "Midterm", date: "2025-07-01", class: "Grade 11A", status: "Scheduled" },
            { id: 4, name: "Final", date: "2025-12-01", class: "Grade 11B", status: "Scheduled" },
            { id: 5, name: "Midterm", date: "2025-07-01", class: "Grade 12A", status: "Scheduled" }
        ],
        analytics: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            data: [85, 88, 90, 87, 89, 91]
        }
    },
    student: {
        timetable: [
            { id: 1, day: "Monday", time: "09:00-10:00", subject: "Math", teacher: "John Doe" },
            { id: 2, day: "Monday", time: "10:00-11:00", subject: "Science", teacher: "Jane Smith" },
            { id: 3, day: "Tuesday", time: "09:00-10:00", subject: "English", teacher: "Emily Davis" },
            { id: 4, day: "Tuesday", time: "10:00-11:00", subject: "History", teacher: "Robert Wilson" },
            { id: 5, day: "Wednesday", time: "09:00-10:00", subject: "Math", teacher: "John Doe" }
        ],
        results: [
            { id: 1, exam: "Midterm", subject: "Math", marks: 85, grade: "A" },
            { id: 2, exam: "Midterm", subject: "Science", marks: 78, grade: "B" },
            { id: 3, exam: "Final", subject: "English", marks: 92, grade: "A" },
            { id: 4, exam: "Final", subject: "History", marks: 80, grade: "B" },
            { id: 5, exam: "Midterm", subject: "Math", marks: 88, grade: "A" }
        ],
        homework: [
            { id: 1, subject: "Math", assignment: "Algebra Worksheet", dueDate: "2025-06-15", status: "Pending" },
            { id: 2, subject: "Science", assignment: "Lab Report", dueDate: "2025-06-16", status: "Submitted" },
            { id: 3, subject: "English", assignment: "Essay", dueDate: "2025-06-17", status: "Pending" },
            { id: 4, subject: "History", assignment: "Project", dueDate: "2025-06-18", status: "Submitted" },
            { id: 5, subject: "Math", assignment: "Geometry Worksheet", dueDate: "2025-06-19", status: "Pending" }
        ],
        analytics: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            data: [80, 82, 85, 88, 90, 92]
        }
    },
    parent: {
        attendance: [
            { id: 1, date: "2025-06-10", status: "Present", class: "Grade 10A" },
            { id: 2, date: "2025-06-11", status: "Absent", class: "Grade 10A" },
            { id: 3, date: "2025-06-12", status: "Present", class: "Grade 10A" },
            { id: 4, date: "2025-06-13", status: "Present", class: "Grade 10A" },
            { id: 5, date: "2025-06-14", status: "Absent", class: "Grade 10A" }
        ],
        fees: [
            { id: 1, amount: 1000, status: "Paid", date: "2025-06-01" },
            { id: 2, amount: 1200, status: "Pending", date: "2025-06-05" },
            { id: 3, amount: 1000, status: "Paid", date: "2025-06-03" },
            { id: 4, amount: 1100, status: "Pending", date: "2025-06-07" },
            { id: 5, amount: 1000, status: "Paid", date: "2025-06-02" }
        ],
        progress: [
            { id: 1, exam: "Midterm", subject: "Math", marks: 85, grade: "A" },
            { id: 2, exam: "Midterm", subject: "Science", marks: 78, grade: "B" },
            { id: 3, exam: "Final", subject: "English", marks: 92, grade: "A" },
            { id: 4, exam: "Final", subject: "History", marks: 80, grade: "B" },
            { id: 5, exam: "Midterm", subject: "Math", marks: 88, grade: "A" }
        ],
        analytics: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            data: [80, 82, 85, 88, 90, 92]
        }
    }
};

function renderTable(section, data, page = 1, filter = '', query = '') {
    const itemsPerPage = 3;
    const filteredData = data.filter(item => {
        if (filter && section.includes('institutes') && item.location !== filter) return false;
        if (filter && section.includes('classes') && item.name !== filter) return false;
        if (filter && section.includes('attendance') && item.class !== filter) return false;
        if (filter && section.includes('homework') && item.subject !== filter) return false;
        if (query) {
            return Object.values(item).some(val => 
                val.toString().toLowerCase().includes(query.toLowerCase())
            );
        }
        return true;
    });

    const start = (page - 1) * itemsPerPage;
    const paginatedData = filteredData.slice(start, start + itemsPerPage);
    const tableBody = document.getElementById(`${section}-table`);
    tableBody.innerHTML = '';

    paginatedData.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = section.includes('institutes') ? `
            <td>${item.name}</td>
            <td>${item.location}</td>
            <td>${item.students}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Institute: ${item.name}', 'Location: ${item.location}<br>Students: ${item.students}')">View</button></td>
        ` : section.includes('users') ? `
            <td>${item.name}</td>
            <td>${item.role}</td>
            <td>${item.institute}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('User: ${item.name}', 'Role: ${item.role}<br>Institute: ${item.institute}')">View</button></td>
        ` : section.includes('classes') ? `
            <td>${item.name}</td>
            <td>${item.teacher}</td>
            <td>${item.students}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Class: ${item.name}', 'Teacher: ${item.teacher}<br>Students: ${item.students}')">View</button></td>
        ` : section.includes('fees') ? `
            <td>${item.student || item.amount}</td>
            <td>${item.amount || item.status}</td>
            <td>${item.status || item.date}</td>
            <td>${item.date || ''}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Fee Details', 'Student: ${item.student || 'N/A'}<br>Amount: $${item.amount}<br>Status: ${item.status}<br>Date: ${item.date}')">View</button></td>
        ` : section.includes('attendance') ? `
            <td>${item.student || item.date}</td>
            <td>${item.date || item.status}</td>
            <td>${item.status || item.class}</td>
            <td>${item.class ? `<button class="btn btn-primary btn-sm" onclick="showDetails('Attendance: ${item.student || item.date}', 'Date: ${item.date}<br>Status: ${item.status}<br>Class: ${item.class}')">View</button>` : ''}</td>
        ` : section.includes('schedule') ? `
            <td>${item.day}</td>
            <td>${item.time}</td>
            <td>${item.class}</td>
            <td>${item.subject}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Schedule: ${item.class}', 'Day: ${item.day}<br>Time: ${item.time}<br>Subject: ${item.subject}')">View</button></td>
        ` : section.includes('exams') ? `
            <td>${item.name}</td>
            <td>${item.date}</td>
            <td>${item.class}</td>
            <td>${item.status}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Exam: ${item.name}', 'Date: ${item.date}<br>Class: ${item.class}<br>Status: ${item.status}')">View</button></td>
        ` : section.includes('timetable') ? `
            <td>${item.day}</td>
            <td>${item.time}</td>
            <td>${item.subject}</td>
            <td>${item.teacher}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Timetable: ${item.subject}', 'Day: ${item.day}<br>Time: ${item.time}<br>Teacher: ${item.teacher}')">View</button></td>
        ` : section.includes('results') ? `
            <td>${item.exam}</td>
            <td>${item.subject}</td>
            <td>${item.marks}</td>
            <td>${item.grade}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Result: ${item.exam}', 'Subject: ${item.subject}<br>Marks: ${item.marks}<br>Grade: ${item.grade}')">View</button></td>
        ` : section.includes('homework') ? `
            <td>${item.subject}</td>
            <td>${item.assignment}</td>
            <td>${item.dueDate}</td>
            <td>${item.status}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Homework: ${item.assignment}', 'Subject: ${item.subject}<br>Due Date: ${item.dueDate}<br>Status: ${item.status}')">View</button></td>
        ` : section.includes('progress') ? `
            <td>${item.exam}</td>
            <td>${item.subject}</td>
            <td>${item.marks}</td>
            <td>${item.grade}</td>
            <td><button class="btn btn-primary btn-sm" onclick="showDetails('Progress: ${item.exam}', 'Subject: ${item.subject}<br>Marks: ${item.marks}<br>Grade: ${item.grade}')">View</button></td>
        ` : '';
        tableBody.appendChild(row);
    });

    // Pagination
    const totalPages = Math.ceil(filteredData.length / itemsPerPage);
    const pagination = document.getElementById(`${section}-pagination`);
    pagination.innerHTML = '';
    for (let i = 1; i <= totalPages; i++) {
        const li = document.createElement('li');
        li.className = `page-item ${i === page ? 'active' : ''}`;
        li.innerHTML = `<a class="page-link" href="#">${i}</a>`;
        li.addEventListener('click', (e) => {
            e.preventDefault();
            renderTable(section, data, i, filter, query);
        });
        pagination.appendChild(li);
    }
}

function showDetails(title, content) {
    window.dispatchEvent(new CustomEvent('showDetails', { detail: { title, content } }));
}

function renderChart(canvasId, labels, data, label) {
    new Chart(document.getElementById(canvasId), {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                borderColor: '#87CEEB',
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const path = window.location.pathname.split('/').pop();
    const role = path.replace('demo_', '');
    const data = demoData[role] || {};

    // Render initial tables and charts
    if (data.institutes) renderTable('institutes', data.institutes);
    if (data.users) renderTable('users', data.users);
    if (data.classes) renderTable('classes', data.classes);
    if (data.fees) renderTable('fees', data.fees);
    if (data.attendance) renderTable('attendance', data.attendance);
    if (data.schedule) renderTable('schedule', data.schedule);
    if (data.exams) renderTable('exams', data.exams);
    if (data.timetable) renderTable('timetable', data.timetable);
    if (data.results) renderTable('results', data.results);
    if (data.homework) renderTable('homework', data.homework);
    if (data.progress) renderTable('progress', data.progress);
    if (data.analytics) {
        renderChart('analytics-chart', data.analytics.labels, data.analytics.data, 'Performance');
        if (document.getElementById('detailed-analytics-chart')) {
            renderChart('detailed-analytics-chart', data.analytics.labels, data.analytics.data, 'Detailed Performance');
        }
    }

    // Handle search and filter events
    window.addEventListener('searchData', (e) => {
        const { query, section } = e.detail;
        if (data[section]) renderTable(section, data[section], 1, '', query);
    });

    window.addEventListener('filterData', (e) => {
        const { section, value } = e.detail;
        if (data[section]) renderTable(section, data[section], 1, value);
    });
});