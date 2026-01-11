public class Student {

    private int id;
    private String name;
    private int age;
    private String gender;
    private String email;
    private String phone;
    private String course;
    private int yearOfStudy;
    private String address;

    public Student(String name, int age, String gender, String email,
                   String phone, String course, int yearOfStudy, String address) {
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.email = email;
        this.phone = phone;
        this.course = course;
        this.yearOfStudy = yearOfStudy;
        this.address = address;
    }

    public Student(int id, String name, int age, String gender, String email,
                   String phone, String course, int yearOfStudy, String address) {
        this(name, age, gender, email, phone, course, yearOfStudy, address);
        this.id = id;
    }

    // getters
    public int getId() { return id; }
    public String getName() { return name; }
    public int getAge() { return age; }
    public String getGender() { return gender; }
    public String getEmail() { return email; }
    public String getPhone() { return phone; }
    public String getCourse() { return course; }
    public int getYearOfStudy() { return yearOfStudy; }
    public String getAddress() { return address; }
}
