.class public Lcom/android/calculator2/Calculator;
.super Landroid/app/Activity;
.source "Calculator.java"

# interfaces
.implements Lcom/android/calculator2/PanelSwitcher$Listener;
.implements Lcom/android/calculator2/Logic$Listener;
.implements Landroid/view/View$OnClickListener;
.implements Landroid/widget/PopupMenu$OnMenuItemClickListener;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/calculator2/Calculator$PageAdapter;
    }
.end annotation


# static fields
.field static final ADVANCED_PANEL:I = 0x1

.field static final BASIC_PANEL:I = 0x0

.field private static final DEBUG:Z = false

.field private static final LOG_ENABLED:Z = false

.field private static final LOG_TAG:Ljava/lang/String; = "Calculator"

.field private static final STATE_CURRENT_VIEW:Ljava/lang/String; = "state-current-view"


# instance fields
.field private mBackspaceButton:Landroid/view/View;

.field private mClearButton:Landroid/view/View;

.field private mDisplay:Lcom/android/calculator2/CalculatorDisplay;

.field private mHistory:Lcom/android/calculator2/History;

.field mListener:Lcom/android/calculator2/EventListener;

.field private mLogic:Lcom/android/calculator2/Logic;

.field private mOverflowMenuButton:Landroid/view/View;

.field private mPager:Landroid/support/v4/view/ViewPager;

.field private mPersist:Lcom/android/calculator2/Persist;


# direct methods
.method public constructor <init>()V
    .locals 1

    .prologue
    .line 39
    invoke-direct {p0}, Landroid/app/Activity;-><init>()V

    .line 41
    new-instance v0, Lcom/android/calculator2/EventListener;

    invoke-direct {v0}, Lcom/android/calculator2/EventListener;-><init>()V

    iput-object v0, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    .line 261
    return-void
.end method

.method static synthetic access$002(Lcom/android/calculator2/Calculator;Landroid/view/View;)Landroid/view/View;
    .locals 0
    .parameter "x0"
    .parameter "x1"

    .prologue
    .line 39
    iput-object p1, p0, Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;

    return-object p1
.end method

.method static synthetic access$102(Lcom/android/calculator2/Calculator;Landroid/view/View;)Landroid/view/View;
    .locals 0
    .parameter "x0"
    .parameter "x1"

    .prologue
    .line 39
    iput-object p1, p0, Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;

    return-object p1
.end method

.method private constructPopupMenu()Landroid/widget/PopupMenu;
    .locals 3

    .prologue
    .line 174
    new-instance v1, Landroid/widget/PopupMenu;

    iget-object v2, p0, Lcom/android/calculator2/Calculator;->mOverflowMenuButton:Landroid/view/View;

    invoke-direct {v1, p0, v2}, Landroid/widget/PopupMenu;-><init>(Landroid/content/Context;Landroid/view/View;)V

    .line 175
    .local v1, popupMenu:Landroid/widget/PopupMenu;
    invoke-virtual {v1}, Landroid/widget/PopupMenu;->getMenu()Landroid/view/Menu;

    move-result-object v0

    .line 176
    .local v0, menu:Landroid/view/Menu;
    const/high16 v2, 0x7f0b

    invoke-virtual {v1, v2}, Landroid/widget/PopupMenu;->inflate(I)V

    .line 177
    invoke-virtual {v1, p0}, Landroid/widget/PopupMenu;->setOnMenuItemClickListener(Landroid/widget/PopupMenu$OnMenuItemClickListener;)V

    .line 178
    invoke-virtual {p0, v0}, Lcom/android/calculator2/Calculator;->onPrepareOptionsMenu(Landroid/view/Menu;)Z

    .line 179
    return-object v1
.end method

.method private createFakeMenu()V
    .locals 2

    .prologue
    .line 154
    const v0, 0x7f0c0010

    invoke-virtual {p0, v0}, Lcom/android/calculator2/Calculator;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/android/calculator2/Calculator;->mOverflowMenuButton:Landroid/view/View;

    .line 155
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mOverflowMenuButton:Landroid/view/View;

    if-eqz v0, :cond_0

    .line 156
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mOverflowMenuButton:Landroid/view/View;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    .line 157
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mOverflowMenuButton:Landroid/view/View;

    invoke-virtual {v0, p0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 159
    :cond_0
    return-void
.end method

.method private getAdvancedVisibility()Z
    .locals 2

    .prologue
    const/4 v0, 0x1

    .line 193
    iget-object v1, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    invoke-virtual {v1}, Landroid/support/v4/view/ViewPager;->getCurrentItem()I

    move-result v1

    if-ne v1, v0, :cond_0

    :goto_0
    return v0

    :cond_0
    const/4 v0, 0x0

    goto :goto_0
.end method

.method private getBasicVisibility()Z
    .locals 1

    .prologue
    .line 189
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    invoke-virtual {v0}, Landroid/support/v4/view/ViewPager;->getCurrentItem()I

    move-result v0

    if-nez v0, :cond_0

    const/4 v0, 0x1

    :goto_0
    return v0

    :cond_0
    const/4 v0, 0x0

    goto :goto_0
.end method

.method static log(Ljava/lang/String;)V
    .locals 0
    .parameter "message"

    .prologue
    .line 249
    return-void
.end method

.method private updateDeleteMode()V
    .locals 3

    .prologue
    const/16 v2, 0x8

    const/4 v1, 0x0

    .line 123
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    invoke-virtual {v0}, Lcom/android/calculator2/Logic;->getDeleteMode()I

    move-result v0

    if-nez v0, :cond_0

    .line 124
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;

    invoke-virtual {v0, v2}, Landroid/view/View;->setVisibility(I)V

    .line 125
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    .line 130
    :goto_0
    return-void

    .line 127
    :cond_0
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;

    invoke-virtual {v0, v1}, Landroid/view/View;->setVisibility(I)V

    .line 128
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;

    invoke-virtual {v0, v2}, Landroid/view/View;->setVisibility(I)V

    goto :goto_0
.end method


# virtual methods
.method public onChange()V
    .locals 0

    .prologue
    .line 253
    invoke-virtual {p0}, Lcom/android/calculator2/Calculator;->invalidateOptionsMenu()V

    .line 254
    return-void
.end method

.method public onClick(Landroid/view/View;)V
    .locals 2
    .parameter "v"

    .prologue
    .line 163
    invoke-virtual {p1}, Landroid/view/View;->getId()I

    move-result v1

    packed-switch v1, :pswitch_data_0

    .line 171
    :cond_0
    :goto_0
    return-void

    .line 165
    :pswitch_0
    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->constructPopupMenu()Landroid/widget/PopupMenu;

    move-result-object v0

    .line 166
    .local v0, menu:Landroid/widget/PopupMenu;
    if-eqz v0, :cond_0

    .line 167
    invoke-virtual {v0}, Landroid/widget/PopupMenu;->show()V

    goto :goto_0

    .line 163
    :pswitch_data_0
    .packed-switch 0x7f0c0010
        :pswitch_0
    .end packed-switch
.end method

.method public onCreate(Landroid/os/Bundle;)V
    .locals 7
    .parameter "state"

    .prologue
    const/high16 v5, 0x2

    const/4 v4, 0x0

    .line 61
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    .line 64
    invoke-virtual {p0}, Lcom/android/calculator2/Calculator;->getWindow()Landroid/view/Window;

    move-result-object v3

    invoke-virtual {v3, v5, v5}, Landroid/view/Window;->setFlags(II)V

    .line 67
    const v3, 0x7f040002

    invoke-virtual {p0, v3}, Lcom/android/calculator2/Calculator;->setContentView(I)V

    .line 68
    const v3, 0x7f0c0013

    invoke-virtual {p0, v3}, Lcom/android/calculator2/Calculator;->findViewById(I)Landroid/view/View;

    move-result-object v3

    check-cast v3, Landroid/support/v4/view/ViewPager;

    iput-object v3, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    .line 69
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    if-eqz v3, :cond_4

    .line 70
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    new-instance v5, Lcom/android/calculator2/Calculator$PageAdapter;

    iget-object v6, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    invoke-direct {v5, p0, v6}, Lcom/android/calculator2/Calculator$PageAdapter;-><init>(Lcom/android/calculator2/Calculator;Landroid/support/v4/view/ViewPager;)V

    invoke-virtual {v3, v5}, Landroid/support/v4/view/ViewPager;->setAdapter(Landroid/support/v4/view/PagerAdapter;)V

    .line 80
    :goto_0
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;

    if-nez v3, :cond_0

    .line 81
    const v3, 0x7f0c0011

    invoke-virtual {p0, v3}, Lcom/android/calculator2/Calculator;->findViewById(I)Landroid/view/View;

    move-result-object v3

    iput-object v3, p0, Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;

    .line 82
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    invoke-virtual {v3, v5}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 83
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mClearButton:Landroid/view/View;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    invoke-virtual {v3, v5}, Landroid/view/View;->setOnLongClickListener(Landroid/view/View$OnLongClickListener;)V

    .line 85
    :cond_0
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;

    if-nez v3, :cond_1

    .line 86
    const v3, 0x7f0c0012

    invoke-virtual {p0, v3}, Lcom/android/calculator2/Calculator;->findViewById(I)Landroid/view/View;

    move-result-object v3

    iput-object v3, p0, Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;

    .line 87
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    invoke-virtual {v3, v5}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 88
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mBackspaceButton:Landroid/view/View;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    invoke-virtual {v3, v5}, Landroid/view/View;->setOnLongClickListener(Landroid/view/View$OnLongClickListener;)V

    .line 91
    :cond_1
    new-instance v3, Lcom/android/calculator2/Persist;

    invoke-direct {v3, p0}, Lcom/android/calculator2/Persist;-><init>(Landroid/content/Context;)V

    iput-object v3, p0, Lcom/android/calculator2/Calculator;->mPersist:Lcom/android/calculator2/Persist;

    .line 92
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mPersist:Lcom/android/calculator2/Persist;

    invoke-virtual {v3}, Lcom/android/calculator2/Persist;->load()V

    .line 94
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mPersist:Lcom/android/calculator2/Persist;

    iget-object v3, v3, Lcom/android/calculator2/Persist;->history:Lcom/android/calculator2/History;

    iput-object v3, p0, Lcom/android/calculator2/Calculator;->mHistory:Lcom/android/calculator2/History;

    .line 96
    const v3, 0x7f0c000f

    invoke-virtual {p0, v3}, Lcom/android/calculator2/Calculator;->findViewById(I)Landroid/view/View;

    move-result-object v3

    check-cast v3, Lcom/android/calculator2/CalculatorDisplay;

    iput-object v3, p0, Lcom/android/calculator2/Calculator;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    .line 98
    new-instance v3, Lcom/android/calculator2/Logic;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mHistory:Lcom/android/calculator2/History;

    iget-object v6, p0, Lcom/android/calculator2/Calculator;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    invoke-direct {v3, p0, v5, v6}, Lcom/android/calculator2/Logic;-><init>(Landroid/content/Context;Lcom/android/calculator2/History;Lcom/android/calculator2/CalculatorDisplay;)V

    iput-object v3, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    .line 99
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    invoke-virtual {v3, p0}, Lcom/android/calculator2/Logic;->setListener(Lcom/android/calculator2/Logic$Listener;)V

    .line 101
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mPersist:Lcom/android/calculator2/Persist;

    invoke-virtual {v5}, Lcom/android/calculator2/Persist;->getDeleteMode()I

    move-result v5

    invoke-virtual {v3, v5}, Lcom/android/calculator2/Logic;->setDeleteMode(I)V

    .line 102
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    invoke-virtual {v5}, Lcom/android/calculator2/CalculatorDisplay;->getMaxDigits()I

    move-result v5

    invoke-virtual {v3, v5}, Lcom/android/calculator2/Logic;->setLineLength(I)V

    .line 104
    new-instance v1, Lcom/android/calculator2/HistoryAdapter;

    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mHistory:Lcom/android/calculator2/History;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    invoke-direct {v1, p0, v3, v5}, Lcom/android/calculator2/HistoryAdapter;-><init>(Landroid/content/Context;Lcom/android/calculator2/History;Lcom/android/calculator2/Logic;)V

    .line 105
    .local v1, historyAdapter:Lcom/android/calculator2/HistoryAdapter;
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v3, v1}, Lcom/android/calculator2/History;->setObserver(Landroid/widget/BaseAdapter;)V

    .line 107
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    if-eqz v3, :cond_2

    .line 108
    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    if-nez p1, :cond_6

    move v3, v4

    :goto_1
    invoke-virtual {v5, v3}, Landroid/support/v4/view/ViewPager;->setCurrentItem(I)V

    .line 111
    :cond_2
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    iget-object v4, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    iget-object v5, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    invoke-virtual {v3, v4, v5}, Lcom/android/calculator2/EventListener;->setHandler(Lcom/android/calculator2/Logic;Landroid/support/v4/view/ViewPager;)V

    .line 112
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mDisplay:Lcom/android/calculator2/CalculatorDisplay;

    iget-object v4, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    invoke-virtual {v3, v4}, Lcom/android/calculator2/CalculatorDisplay;->setOnKeyListener(Landroid/view/View$OnKeyListener;)V

    .line 114
    invoke-static {p0}, Landroid/view/ViewConfiguration;->get(Landroid/content/Context;)Landroid/view/ViewConfiguration;

    move-result-object v3

    invoke-virtual {v3}, Landroid/view/ViewConfiguration;->hasPermanentMenuKey()Z

    move-result v3

    if-nez v3, :cond_3

    .line 115
    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->createFakeMenu()V

    .line 118
    :cond_3
    iget-object v3, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    invoke-virtual {v3}, Lcom/android/calculator2/Logic;->resumeWithHistory()V

    .line 119
    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->updateDeleteMode()V

    .line 120
    return-void

    .line 73
    .end local v1           #historyAdapter:Lcom/android/calculator2/HistoryAdapter;
    :cond_4
    invoke-virtual {p0}, Lcom/android/calculator2/Calculator;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    const v5, 0x7f050002

    invoke-virtual {v3, v5}, Landroid/content/res/Resources;->obtainTypedArray(I)Landroid/content/res/TypedArray;

    move-result-object v0

    .line 74
    .local v0, buttons:Landroid/content/res/TypedArray;
    const/4 v2, 0x0

    .local v2, i:I
    :goto_2
    invoke-virtual {v0}, Landroid/content/res/TypedArray;->length()I

    move-result v3

    if-ge v2, v3, :cond_5

    .line 75
    const/4 v3, 0x0

    invoke-virtual {v0, v2, v4}, Landroid/content/res/TypedArray;->getResourceId(II)I

    move-result v5

    invoke-virtual {p0, v3, v5}, Lcom/android/calculator2/Calculator;->setOnClickListener(Landroid/view/View;I)V

    .line 74
    add-int/lit8 v2, v2, 0x1

    goto :goto_2

    .line 77
    :cond_5
    invoke-virtual {v0}, Landroid/content/res/TypedArray;->recycle()V

    goto/16 :goto_0

    .line 108
    .end local v0           #buttons:Landroid/content/res/TypedArray;
    .end local v2           #i:I
    .restart local v1       #historyAdapter:Lcom/android/calculator2/HistoryAdapter;
    :cond_6
    const-string v3, "state-current-view"

    invoke-virtual {p1, v3, v4}, Landroid/os/Bundle;->getInt(Ljava/lang/String;I)I

    move-result v3

    goto :goto_1
.end method

.method public onCreateOptionsMenu(Landroid/view/Menu;)Z
    .locals 2
    .parameter "menu"

    .prologue
    .line 139
    invoke-super {p0, p1}, Landroid/app/Activity;->onCreateOptionsMenu(Landroid/view/Menu;)Z

    .line 140
    invoke-virtual {p0}, Lcom/android/calculator2/Calculator;->getMenuInflater()Landroid/view/MenuInflater;

    move-result-object v0

    const/high16 v1, 0x7f0b

    invoke-virtual {v0, v1, p1}, Landroid/view/MenuInflater;->inflate(ILandroid/view/Menu;)V

    .line 141
    const/4 v0, 0x1

    return v0
.end method

.method public onDeleteModeChange()V
    .locals 0

    .prologue
    .line 258
    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->updateDeleteMode()V

    .line 259
    return-void
.end method

.method public onKeyDown(ILandroid/view/KeyEvent;)Z
    .locals 2
    .parameter "keyCode"
    .parameter "keyEvent"

    .prologue
    .line 237
    const/4 v0, 0x4

    if-ne p1, v0, :cond_0

    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->getAdvancedVisibility()Z

    move-result v0

    if-eqz v0, :cond_0

    .line 238
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/support/v4/view/ViewPager;->setCurrentItem(I)V

    .line 239
    const/4 v0, 0x1

    .line 241
    :goto_0
    return v0

    :cond_0
    invoke-super {p0, p1, p2}, Landroid/app/Activity;->onKeyDown(ILandroid/view/KeyEvent;)Z

    move-result v0

    goto :goto_0
.end method

.method public onMenuItemClick(Landroid/view/MenuItem;)Z
    .locals 1
    .parameter "item"

    .prologue
    .line 185
    invoke-virtual {p0, p1}, Lcom/android/calculator2/Calculator;->onOptionsItemSelected(Landroid/view/MenuItem;)Z

    move-result v0

    return v0
.end method

.method public onOptionsItemSelected(Landroid/view/MenuItem;)Z
    .locals 2
    .parameter "item"

    .prologue
    .line 198
    invoke-interface {p1}, Landroid/view/MenuItem;->getItemId()I

    move-result v0

    packed-switch v0, :pswitch_data_0

    .line 216
    :cond_0
    :goto_0
    invoke-super {p0, p1}, Landroid/app/Activity;->onOptionsItemSelected(Landroid/view/MenuItem;)Z

    move-result v0

    return v0

    .line 200
    :pswitch_0
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mHistory:Lcom/android/calculator2/History;

    invoke-virtual {v0}, Lcom/android/calculator2/History;->clear()V

    .line 201
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    invoke-virtual {v0}, Lcom/android/calculator2/Logic;->onClear()V

    goto :goto_0

    .line 205
    :pswitch_1
    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->getBasicVisibility()Z

    move-result v0

    if-nez v0, :cond_0

    .line 206
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/support/v4/view/ViewPager;->setCurrentItem(I)V

    goto :goto_0

    .line 211
    :pswitch_2
    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->getAdvancedVisibility()Z

    move-result v0

    if-nez v0, :cond_0

    .line 212
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Landroid/support/v4/view/ViewPager;->setCurrentItem(I)V

    goto :goto_0

    .line 198
    nop

    :pswitch_data_0
    .packed-switch 0x7f0c0025
        :pswitch_0
        :pswitch_2
        :pswitch_1
    .end packed-switch
.end method

.method public onPause()V
    .locals 2

    .prologue
    .line 229
    invoke-super {p0}, Landroid/app/Activity;->onPause()V

    .line 230
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    invoke-virtual {v0}, Lcom/android/calculator2/Logic;->updateHistory()V

    .line 231
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPersist:Lcom/android/calculator2/Persist;

    iget-object v1, p0, Lcom/android/calculator2/Calculator;->mLogic:Lcom/android/calculator2/Logic;

    invoke-virtual {v1}, Lcom/android/calculator2/Logic;->getDeleteMode()I

    move-result v1

    invoke-virtual {v0, v1}, Lcom/android/calculator2/Persist;->setDeleteMode(I)V

    .line 232
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPersist:Lcom/android/calculator2/Persist;

    invoke-virtual {v0}, Lcom/android/calculator2/Persist;->save()V

    .line 233
    return-void
.end method

.method public onPrepareOptionsMenu(Landroid/view/Menu;)Z
    .locals 4
    .parameter "menu"

    .prologue
    const/4 v2, 0x0

    const/4 v1, 0x1

    .line 146
    invoke-super {p0, p1}, Landroid/app/Activity;->onPrepareOptionsMenu(Landroid/view/Menu;)Z

    .line 147
    const v0, 0x7f0c0027

    invoke-interface {p1, v0}, Landroid/view/Menu;->findItem(I)Landroid/view/MenuItem;

    move-result-object v3

    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->getBasicVisibility()Z

    move-result v0

    if-nez v0, :cond_1

    move v0, v1

    :goto_0
    invoke-interface {v3, v0}, Landroid/view/MenuItem;->setVisible(Z)Landroid/view/MenuItem;

    .line 148
    const v0, 0x7f0c0026

    invoke-interface {p1, v0}, Landroid/view/Menu;->findItem(I)Landroid/view/MenuItem;

    move-result-object v0

    invoke-direct {p0}, Lcom/android/calculator2/Calculator;->getAdvancedVisibility()Z

    move-result v3

    if-nez v3, :cond_0

    move v2, v1

    :cond_0
    invoke-interface {v0, v2}, Landroid/view/MenuItem;->setVisible(Z)Landroid/view/MenuItem;

    .line 149
    return v1

    :cond_1
    move v0, v2

    .line 147
    goto :goto_0
.end method

.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .locals 2
    .parameter "state"

    .prologue
    .line 221
    invoke-super {p0, p1}, Landroid/app/Activity;->onSaveInstanceState(Landroid/os/Bundle;)V

    .line 222
    iget-object v0, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    if-eqz v0, :cond_0

    .line 223
    const-string v0, "state-current-view"

    iget-object v1, p0, Lcom/android/calculator2/Calculator;->mPager:Landroid/support/v4/view/ViewPager;

    invoke-virtual {v1}, Landroid/support/v4/view/ViewPager;->getCurrentItem()I

    move-result v1

    invoke-virtual {p1, v0, v1}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    .line 225
    :cond_0
    return-void
.end method

.method setOnClickListener(Landroid/view/View;I)V
    .locals 2
    .parameter "root"
    .parameter "id"

    .prologue
    .line 133
    if-eqz p1, :cond_0

    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    .line 134
    .local v0, target:Landroid/view/View;
    :goto_0
    iget-object v1, p0, Lcom/android/calculator2/Calculator;->mListener:Lcom/android/calculator2/EventListener;

    invoke-virtual {v0, v1}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 135
    return-void

    .line 133
    .end local v0           #target:Landroid/view/View;
    :cond_0
    invoke-virtual {p0, p2}, Lcom/android/calculator2/Calculator;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_0
.end method
