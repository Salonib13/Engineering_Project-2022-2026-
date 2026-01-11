import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        StudentDAO dao = new StudentDAO();
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- student management system ---");
            System.out.println("1. add student");
            System.out.println("2. view all students");
            System.out.println("3. delete student");
            System.out.println("4. exit");
            System.out.print("enter choice: ");

            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {

                case 1:
                    System.out.print("name: ");
                    String name = sc.nextLine();

                    System.out.print("age: ");
                    int age = sc.nextInt();
                    sc.nextLine();

                    System.out.print("gender: ");
                    String gender = sc.nextLine();

                    System.out.print("email: ");
                    String email = sc.nextLine();

                    System.out.print("phone: ");
                    String phone = sc.nextLine();

                    System.out.print("course: ");
                    String course = sc.nextLine();

                    System.out.print("year of study: ");
                    int year = sc.nextInt();
                    sc.nextLine();

                    System.out.print("address: ");
                    String address = sc.nextLine();

                    Student s = new Student(name, age, gender, email, phone, course, year, address);
                    dao.addStudent(s);
                    break;

                case 2:
                    List<Student> students = dao.getAllStudents();
                    for (Student st : students) {
                        System.out.println(
                                st.getId() + " | " +
                                st.getName() + " | " +
                                st.getCourse() + " | year " +
                                st.getYearOfStudy()
                        );
                    }
                    break;

                case 3:
                    System.out.print("enter student id to delete: ");
                    int id = sc.nextInt();
                    dao.deleteStudent(id);
                    break;

                case 4:
                    System.out.println("exit successful");
                    System.exit(0);

                default:
                    System.out.println("invalid choice");
            }
        }
    }
}
