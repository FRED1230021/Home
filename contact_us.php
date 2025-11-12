<?php
// 1. Database Connection Details
$host = 'localhost'; // Your database host (often 'localhost')
$db   = 'contact_message'; // The name of your database
$user = 'root'; // Your database username
$pass = ''; // Your database password
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Attempt to establish a connection to the database
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // If connection fails, stop execution and display an error
    die("Database connection failed: " . $e->getMessage());
}

// 2. Check for Form Submission
// Ensure the form was submitted using the POST method
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // 3. Retrieve and Sanitize Form Data
    // Use the null-coalescing operator (??) to prevent 'undefined index' errors
    $location = $_POST['location'] ?? '';
    $email = $_POST['email'] ?? '';
    $message = $_POST['message'] ?? '';
    
    // Optional: Basic validation to ensure fields aren't empty
    if (empty($location) || empty($email) || empty($message)) {
        // Redirect back or display an error if fields are missing
        header("Location: contact_us.html?status=error&message=All fields are required.");
        exit;
    }

    // 4. SQL INSERT Statement (using Prepared Statements for security)
    $sql = "INSERT INTO contact_messages (sender_location, sender_email, message_content) 
            VALUES (?, ?, ?)";

    try {
        // Prepare the SQL statement
        $stmt = $pdo->prepare($sql);
        
        // Execute the statement, passing the sanitized user data as an array
        // PDO automatically handles escaping special characters, preventing SQL Injection
        $stmt->execute([$location, $email, $message]);

        // 5. Success Handling and Redirection
        // Redirect the user back to the contact page with a success message
        // This prevents the user from submitting the same form data if they refresh the page (Post/Redirect/Get pattern)
        header("Location: contact_us.html?status=success");
        exit;

    } catch (\PDOException $e) {
        // Handle SQL execution errors
        // Log the error for development purposes, but don't show to the user
        error_log("SQL Error: " . $e->getMessage());
        
        // Redirect with a generic error message
        header("Location: contact_us.html?status=error&message=An internal error occurred.");
        exit;
    }
} else {
    // If the script is accessed directly without POST data
    header("Location: contact_us.html");
 exit;
}
?>
