using System;
using System.Windows;

namespace lab5
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Focus(object sender, EventArgs e)
        {
            ((FrameworkElement)sender).Style = (Style)Resources["Focus"];
        }

        private void FocusOff(object sender, EventArgs e)
        {
            ((FrameworkElement)sender).Style = (Style)Resources["UnFocus"];
        }
    }
}