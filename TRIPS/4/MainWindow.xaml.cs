using System.Windows;
using System.Windows.Controls;

namespace _4
{
    public partial class MainWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        
        private void ChangeBrushSize(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            var slider = (Slider)sender;

            if (InkCanvas != null)
            {
                InkCanvas.DefaultDrawingAttributes.Height = InkCanvas.DefaultDrawingAttributes.Width = slider.Value;
            }
        }
    }
}
