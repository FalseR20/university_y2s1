using System.Windows;
using System.Windows.Media;

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
                "!!!ВНИМАНИЕ!!!!!!ВНИМАНИЕ!!!\n!!!ВНИМАНИЕ!!!!!!ВНИМАНИЕ!!!\n!!!ВНИМАНИЕ!!!!!!ВНИМАНИЕ!!!\nВАЖНАЯ ИНФОРМАЦИЯ О РАЗРАБОТЧИКЕ!",
                "!!!ВНИМАНИЕ!!!",
                MessageBoxButton.YesNo,
                MessageBoxImage.Warning
            );
            MessageBox.Show(
                "Он учится в БрГТУ",
                "Важно",
                MessageBoxButton.OK,
                MessageBoxImage.Information
            );
        }

        private void SetLightTheme(object sender, RoutedEventArgs e)
        {
            Menu1.Background = Brushes.White;
            ToolBar1.Background = Brushes.AliceBlue;
            StatusBar1.Background = Brushes.AliceBlue;
            StatusBar1.Background = Brushes.AliceBlue;
        }

        private void SetDarkTheme(object sender, RoutedEventArgs e)
        {
            Menu1.Background = Brushes.DimGray;
            ToolBar1.Background = Brushes.Gray;
            StatusBar1.Background = Brushes.Gray;
            StatusBar1.Background = Brushes.Gray;
        }

        private void ChangeStatus(object sender, RoutedEventArgs e)
        {
            if (sender.Equals(ButtonLight)) StatusTextBlock1.Text = "Задает светлую тему";
            else if (sender.Equals(ButtonDark)) StatusTextBlock1.Text = "Задает темную тему";
            else if (sender.Equals(ButtonInfo)) StatusTextBlock1.Text = "Показывает информацию о разработчике";
            else if (sender.Equals(ButtonClose)) StatusTextBlock1.Text = "Закрывает окно";
            else if (sender.Equals(Menu1)) StatusTextBlock1.Text = "Меню";
            else if (sender.Equals(ToolBar1)) StatusTextBlock1.Text = "Меню инструментов";
            else if (sender.Equals(StatusTextBlock1)) StatusTextBlock1.Text = "Тут показывается смысл";
        }
    }
}