import javax.swing.JFrame;
import javax.swing.JButton;
import java.awt.GridBagLayout;
class GuiDemo{
    public static void main(String[] args) {
        JFrame frame = new JFrame("houles");
        JButton b = new JButton("lakshman");
        JButton b1 = new JButton("sena");
        JButton b2 = new JButton("python");
        JButton b3 = new JButton("hari");
        JButton b4 = new JButton("babai");
        JButton b5 = new JButton("bhargav");
        JButton b6 = new JButton("ravi");
        JButton b7 = new JButton("eswar");
        JButton b8 = new JButton("pranav");
        frame.setDefaultCloseOperation(1);
        frame.add(b);
        frame.add(b1);
        frame.add(b2);
        frame.add(b3);
        frame.add(b5);
        frame.add(b6);
        frame.add(b7);
        frame.add(b8);
        frame.setSize(700,700);
        frame.setVisible(true);
    }
}

