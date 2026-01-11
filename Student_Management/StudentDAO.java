import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class StudentDAO {

    public void addStudent(Student s) {
        String sql = "insert into students (name, age, gender, email, phone, course, year_of_study, address) values (?,?,?,?,?,?,?,?)";

        try (Connection con = DatabaseConnection.getConnection();
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setString(1, s.getName());
            ps.setInt(2, s.getAge());
            ps.setString(3, s.getGender());
            ps.setString(4, s.getEmail());
            ps.setString(5, s.getPhone());
            ps.setString(6, s.getCourse());
            ps.setInt(7, s.getYearOfStudy());
            ps.setString(8, s.getAddress());

            ps.executeUpdate();
            System.out.println("student added successfully");

        } catch (SQLException e) {
            System.out.println("error while adding student");
        }
    }

    public List<Student> getAllStudents() {
        List<Student> list = new ArrayList<>();
        String sql = "select * from students";

        try (Connection con = DatabaseConnection.getConnection();
             Statement st = con.createStatement();
             ResultSet rs = st.executeQuery(sql)) {

            while (rs.next()) {
                Student s = new Student(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getInt("age"),
                        rs.getString("gender"),
                        rs.getString("email"),
                        rs.getString("phone"),
                        rs.getString("course"),
                        rs.getInt("year_of_study"),
                        rs.getString("address")
                );
                list.add(s);
            }

        } catch (SQLException e) {
            System.out.println("error fetching students");
        }
        return list;
    }

    public void deleteStudent(int id) {
        String sql = "delete from students where id=?";

        try (Connection con = DatabaseConnection.getConnection();
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setInt(1, id);
            ps.executeUpdate();
            System.out.println("student deleted");

        } catch (SQLException e) {
            System.out.println("error deleting student");
        }
    }
}
