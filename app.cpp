#include <wx/wxprec.h>
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

class MyApp: public wxApp {
    public:
        virtual bool OnInit();
};

wxIMPLEMENT_APP(MyApp);

bool MyApp::OnInit() {
    auto dialog = new wxMessageDialog(nullptr, "こんにちはこんにちは");
    dialog->ShowModal();
    return true;
}
