import javax.swing.JFrame;
import javax.swing.JButton;
class GuiDemo{
    public static void main(String[] args) {
        JFrame f = new JFrame("rama");
        JButton button = new JButton("krishna");
        f.setDefaultCloseOperation(1);
        f.add(button);
        f.setSize(400,400);
        f.setVisible(true);
    }
}

