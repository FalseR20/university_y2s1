using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace _3
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void CloseClick(object sender, RoutedEventArgs e)
        {
            Close();
        }

        private void SiteClick(object sender, RoutedEventArgs e)
        {
            MessageBox.Show(
                "!!!ВНИМАНИЕ!!!!!!ВНИМАНИЕ!!!\n!!!ВНИМАНИЕ!!!!!!ВНИМАНИЕ!!!\n!!!ВНИМАНИЕ!!!!!!ВНИМАНИЕ!!!",
                "!!!ВНИМАНИЕ!!!",
                MessageBoxButton.YesNo,
                MessageBoxImage.Warning
            );
            MessageBox.Show(
                "спасибо за внимание",
                "Важно",
                MessageBoxButton.OK,
                MessageBoxImage.Information
            );
        }

        private void SetLightTheme(object sender, RoutedEventArgs e)
        {
            Menu1.Background = Brushes.White;
            ToolBar1.Background = Brushes.AliceBlue;
            StatusBar1.Background = Brushes.White;
        }

        private void SetDarkTheme(object sender, RoutedEventArgs e)
        {
            Menu1.Background = Brushes.DimGray;
            ToolBar1.Background = Brushes.Gray;
            StatusBar1.Background = Brushes.DimGray;
        }

        private void ChangeStatus(object sender, RoutedEventArgs e)
        {
            StatusTextBlock1.Text = e.Source.ToString();
            if (sender.Equals(ButtonLight)) StatusTextBlock2.Text = "Задает светлую тему";
            else if (sender.Equals(ButtonDark)) StatusTextBlock2.Text = "Задает темную тему";
            else if (sender.Equals(ButtonInfo)) StatusTextBlock2.Text = "Показывает информацию о разработчике";
            else if (sender.Equals(ButtonClose)) StatusTextBlock2.Text = "Закрывает окно";
            else if (sender.Equals(Menu1)) StatusTextBlock2.Text = "Меню";
            else if (sender.Equals(ToolBar1)) StatusTextBlock2.Text = "Меню инструментов";

            else if (sender.Equals(StatusTextBlock1)) StatusTextBlock2.Text = "Тут показывается смысл";
            else if (sender.Equals(StatusTextBlock2)) StatusTextBlock2.Text = "Тут выводится угрюмый тип";
            
            
            
        }
    }
}