using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace Lab3_2
{
    public partial class MainWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void ChangeColor(object sender, RoutedEventArgs e)
        {
            var comboBox = (ComboBox)sender;
            var selectedItem = (ComboBoxItem)comboBox.SelectedItem;

            if (InkCanvas != null)
            {
                InkCanvas.DefaultDrawingAttributes.Color = SelectColor(selectedItem.Tag.ToString());
            }

        }

        private Color SelectColor(string color)
        {
            switch (color)
            {
                case "Black":
                    return Colors.Black;
                case "White":
                    return Colors.White;
                case "Red":
                    return Colors.Red;
                case "Green":
                    return Colors.Green;
                case "Blue":
                    return Colors.Blue;
                case "Yellow":
                    return Colors.Yellow;
                default:
                    return Colors.Black;
            }
        }

        private void ChangeBrushSize(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            var slider = (Slider)sender;

            if (InkCanvas != null)
            {
                InkCanvas.DefaultDrawingAttributes.Height = InkCanvas.DefaultDrawingAttributes.Width = slider.Value;
            }
        }

        private void SelectDrawMode(object sender, RoutedEventArgs e)
        {
            if (InkCanvas != null)
            {
                InkCanvas.EditingMode = InkCanvasEditingMode.Ink;
            }
        }

        private void SelectEditMode(object sender, RoutedEventArgs e)
        {
            InkCanvas.EditingMode = InkCanvasEditingMode.Select;
        }

        private void SelectDeleteMode(object sender, RoutedEventArgs e)
        {
            InkCanvas.EditingMode = InkCanvasEditingMode.EraseByPoint;
        }
    }
}