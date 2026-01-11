import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {

    private static final String url =
        "jdbc:mysql://localhost:3306/student_management_system?useSSL=false&serverTimezone=UTC";
    private static final String user = "root";
    private static final String password = "root";

    public static Connection getConnection() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            return DriverManager.getConnection(url, user, password);
        } catch (ClassNotFoundException e) {
            System.out.println("mysql driver not found");
            e.printStackTrace();
            return null;
        } catch (SQLException e) {
            System.out.println("database connection failed");
            e.printStackTrace();
            return null;
        }
    }
}
