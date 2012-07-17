.class public Lcom/android/calculator2/CalculatorEditText;
.super Landroid/widget/EditText;
.source "CalculatorEditText.java"


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/calculator2/CalculatorEditText$1;,
        Lcom/android/calculator2/CalculatorEditText$NoTextSelectionMode;,
        Lcom/android/calculator2/CalculatorEditText$MenuHandler;
    }
.end annotation


# static fields
.field private static final COPY:I = 0x1

.field private static final CUT:I = 0x0

.field private static final LOG_TAG:Ljava/lang/String; = "Calculator2"

.field private static final PASTE:I = 0x2


# instance fields
.field private mMenuItemsStrings:[Ljava/lang/String;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .locals 1
    .parameter "context"
    .parameter "attrs"

    .prologue
    .line 45
    invoke-direct {p0, p1, p2}, Landroid/widget/EditText;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    .line 46
    new-instance v0, Lcom/android/calculator2/CalculatorEditText$NoTextSelectionMode;

    invoke-direct {v0, p0}, Lcom/android/calculator2/CalculatorEditText$NoTextSelectionMode;-><init>(Lcom/android/calculator2/CalculatorEditText;)V

    invoke-virtual {p0, v0}, Lcom/android/calculator2/CalculatorEditText;->setCustomSelectionActionModeCallback(Landroid/view/ActionMode$Callback;)V

    .line 47
    const v0, 0x80001

    invoke-virtual {p0, v0}, Lcom/android/calculator2/CalculatorEditText;->setInputType(I)V

    .line 48
    return-void
.end method

.method static synthetic access$100(Lcom/android/calculator2/CalculatorEditText;)V
    .locals 0
    .parameter "x0"

    .prologue
    .line 36
    invoke-direct {p0}, Lcom/android/calculator2/CalculatorEditText;->copyContent()V

    return-void
.end method

.method private canPaste(Ljava/lang/CharSequence;)Z
    .locals 4
    .parameter "paste"

    .prologue
    .line 155
    const/4 v0, 0x1

    .line 157
    .local v0, canPaste:Z
    :try_start_0
    invoke-virtual {p1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Ljava/lang/Float;->parseFloat(Ljava/lang/String;)F
    :try_end_0
    .catch Ljava/lang/NumberFormatException; {:try_start_0 .. :try_end_0} :catch_0

    .line 162
    :goto_0
    return v0

    .line 158
    :catch_0
    move-exception v1

    .line 159
    .local v1, e:Ljava/lang/NumberFormatException;
    const-string v2, "Calculator2"

    const-string v3, "Error turning string to integer. Ignoring paste."

    invoke-static {v2, v3, v1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    .line 160
    const/4 v0, 0x0

    goto :goto_0
.end method

.method private copyContent()V
    .locals 6

    .prologue
    const/4 v5, 0x0

    .line 117
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getText()Landroid/text/Editable;

    move-result-object v1

    .line 118
    .local v1, text:Landroid/text/Editable;
    invoke-interface {v1}, Landroid/text/Editable;->length()I

    move-result v2

    .line 119
    .local v2, textLength:I
    invoke-virtual {p0, v5, v2}, Lcom/android/calculator2/CalculatorEditText;->setSelection(II)V

    .line 120
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getContext()Landroid/content/Context;

    move-result-object v3

    const-string v4, "clipboard"

    invoke-virtual {v3, v4}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/content/ClipboardManager;

    .line 122
    .local v0, clipboard:Landroid/content/ClipboardManager;
    const/4 v3, 0x0

    invoke-static {v3, v1}, Landroid/content/ClipData;->newPlainText(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/content/ClipData;

    move-result-object v3

    invoke-virtual {v0, v3}, Landroid/content/ClipboardManager;->setPrimaryClip(Landroid/content/ClipData;)V

    .line 123
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getContext()Landroid/content/Context;

    move-result-object v3

    const v4, 0x7f080024

    invoke-static {v3, v4, v5}, Landroid/widget/Toast;->makeText(Landroid/content/Context;II)Landroid/widget/Toast;

    move-result-object v3

    invoke-virtual {v3}, Landroid/widget/Toast;->show()V

    .line 124
    invoke-virtual {p0, v2}, Lcom/android/calculator2/CalculatorEditText;->setSelection(I)V

    .line 125
    return-void
.end method

.method private cutContent()V
    .locals 4

    .prologue
    const/4 v3, 0x0

    .line 128
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getText()Landroid/text/Editable;

    move-result-object v0

    .line 129
    .local v0, text:Landroid/text/Editable;
    invoke-interface {v0}, Landroid/text/Editable;->length()I

    move-result v1

    .line 130
    .local v1, textLength:I
    invoke-virtual {p0, v3, v1}, Lcom/android/calculator2/CalculatorEditText;->setSelection(II)V

    .line 131
    const/4 v2, 0x0

    invoke-static {v2, v0}, Landroid/content/ClipData;->newPlainText(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/content/ClipData;

    move-result-object v2

    invoke-direct {p0, v2}, Lcom/android/calculator2/CalculatorEditText;->setPrimaryClip(Landroid/content/ClipData;)V

    .line 132
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getText()Landroid/text/Editable;

    move-result-object v2

    invoke-interface {v2, v3, v1}, Landroid/text/Editable;->delete(II)Landroid/text/Editable;

    .line 133
    invoke-virtual {p0, v3}, Lcom/android/calculator2/CalculatorEditText;->setSelection(I)V

    .line 134
    return-void
.end method

.method private getPrimaryClip()Landroid/content/ClipData;
    .locals 3

    .prologue
    .line 137
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "clipboard"

    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/content/ClipboardManager;

    .line 139
    .local v0, clipboard:Landroid/content/ClipboardManager;
    invoke-virtual {v0}, Landroid/content/ClipboardManager;->getPrimaryClip()Landroid/content/ClipData;

    move-result-object v1

    return-object v1
.end method

.method private pasteContent()V
    .locals 5

    .prologue
    .line 143
    invoke-direct {p0}, Lcom/android/calculator2/CalculatorEditText;->getPrimaryClip()Landroid/content/ClipData;

    move-result-object v0

    .line 144
    .local v0, clip:Landroid/content/ClipData;
    if-eqz v0, :cond_1

    .line 145
    const/4 v1, 0x0

    .local v1, i:I
    :goto_0
    invoke-virtual {v0}, Landroid/content/ClipData;->getItemCount()I

    move-result v3

    if-ge v1, v3, :cond_1

    .line 146
    invoke-virtual {v0, v1}, Landroid/content/ClipData;->getItemAt(I)Landroid/content/ClipData$Item;

    move-result-object v3

    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getContext()Landroid/content/Context;

    move-result-object v4

    invoke-virtual {v3, v4}, Landroid/content/ClipData$Item;->coerceToText(Landroid/content/Context;)Ljava/lang/CharSequence;

    move-result-object v2

    .line 147
    .local v2, paste:Ljava/lang/CharSequence;
    invoke-direct {p0, v2}, Lcom/android/calculator2/CalculatorEditText;->canPaste(Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_0

    .line 148
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getText()Landroid/text/Editable;

    move-result-object v3

    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getSelectionEnd()I

    move-result v4

    invoke-interface {v3, v4, v2}, Landroid/text/Editable;->insert(ILjava/lang/CharSequence;)Landroid/text/Editable;

    .line 145
    :cond_0
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    .line 152
    .end local v1           #i:I
    .end local v2           #paste:Ljava/lang/CharSequence;
    :cond_1
    return-void
.end method

.method private setPrimaryClip(Landroid/content/ClipData;)V
    .locals 3
    .parameter "clip"

    .prologue
    .line 111
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "clipboard"

    invoke-virtual {v1, v2}, Landroid/content/Context;->getSystemService(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/content/ClipboardManager;

    .line 113
    .local v0, clipboard:Landroid/content/ClipboardManager;
    invoke-virtual {v0, p1}, Landroid/content/ClipboardManager;->setPrimaryClip(Landroid/content/ClipData;)V

    .line 114
    return-void
.end method


# virtual methods
.method public onCreateContextMenu(Landroid/view/ContextMenu;)V
    .locals 9
    .parameter "menu"

    .prologue
    const/4 v8, 0x2

    const/4 v7, 0x1

    const/4 v6, 0x0

    .line 88
    new-instance v0, Lcom/android/calculator2/CalculatorEditText$MenuHandler;

    const/4 v4, 0x0

    invoke-direct {v0, p0, v4}, Lcom/android/calculator2/CalculatorEditText$MenuHandler;-><init>(Lcom/android/calculator2/CalculatorEditText;Lcom/android/calculator2/CalculatorEditText$1;)V

    .line 89
    .local v0, handler:Lcom/android/calculator2/CalculatorEditText$MenuHandler;
    iget-object v4, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    if-nez v4, :cond_0

    .line 90
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    .line 91
    .local v3, resources:Landroid/content/res/Resources;
    const/4 v4, 0x3

    new-array v4, v4, [Ljava/lang/String;

    iput-object v4, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    .line 92
    iget-object v4, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    const v5, 0x1040003

    invoke-virtual {v3, v5}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v5

    aput-object v5, v4, v6

    .line 93
    iget-object v4, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    const v5, 0x1040001

    invoke-virtual {v3, v5}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v5

    aput-object v5, v4, v7

    .line 94
    iget-object v4, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    const v5, 0x104000b

    invoke-virtual {v3, v5}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v5

    aput-object v5, v4, v8

    .line 96
    .end local v3           #resources:Landroid/content/res/Resources;
    :cond_0
    const/4 v1, 0x0

    .local v1, i:I
    :goto_0
    iget-object v4, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    array-length v4, v4

    if-ge v1, v4, :cond_1

    .line 97
    iget-object v4, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    aget-object v4, v4, v1

    invoke-interface {p1, v6, v1, v1, v4}, Landroid/view/ContextMenu;->add(IIILjava/lang/CharSequence;)Landroid/view/MenuItem;

    move-result-object v4

    invoke-interface {v4, v0}, Landroid/view/MenuItem;->setOnMenuItemClickListener(Landroid/view/MenuItem$OnMenuItemClickListener;)Landroid/view/MenuItem;

    .line 96
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    .line 99
    :cond_1
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getText()Landroid/text/Editable;

    move-result-object v4

    invoke-interface {v4}, Landroid/text/Editable;->length()I

    move-result v4

    if-nez v4, :cond_2

    .line 100
    invoke-interface {p1, v6}, Landroid/view/ContextMenu;->getItem(I)Landroid/view/MenuItem;

    move-result-object v4

    invoke-interface {v4, v6}, Landroid/view/MenuItem;->setVisible(Z)Landroid/view/MenuItem;

    .line 101
    invoke-interface {p1, v7}, Landroid/view/ContextMenu;->getItem(I)Landroid/view/MenuItem;

    move-result-object v4

    invoke-interface {v4, v6}, Landroid/view/MenuItem;->setVisible(Z)Landroid/view/MenuItem;

    .line 103
    :cond_2
    invoke-direct {p0}, Lcom/android/calculator2/CalculatorEditText;->getPrimaryClip()Landroid/content/ClipData;

    move-result-object v2

    .line 104
    .local v2, primaryClip:Landroid/content/ClipData;
    if-eqz v2, :cond_3

    invoke-virtual {v2}, Landroid/content/ClipData;->getItemCount()I

    move-result v4

    if-eqz v4, :cond_3

    invoke-virtual {v2, v6}, Landroid/content/ClipData;->getItemAt(I)Landroid/content/ClipData$Item;

    move-result-object v4

    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->getContext()Landroid/content/Context;

    move-result-object v5

    invoke-virtual {v4, v5}, Landroid/content/ClipData$Item;->coerceToText(Landroid/content/Context;)Ljava/lang/CharSequence;

    move-result-object v4

    invoke-direct {p0, v4}, Lcom/android/calculator2/CalculatorEditText;->canPaste(Ljava/lang/CharSequence;)Z

    move-result v4

    if-nez v4, :cond_4

    .line 106
    :cond_3
    invoke-interface {p1, v8}, Landroid/view/ContextMenu;->getItem(I)Landroid/view/MenuItem;

    move-result-object v4

    invoke-interface {v4, v6}, Landroid/view/MenuItem;->setVisible(Z)Landroid/view/MenuItem;

    .line 108
    :cond_4
    return-void
.end method

.method public onTextContextMenuItem(Ljava/lang/CharSequence;)Z
    .locals 3
    .parameter "title"

    .prologue
    .line 72
    const/4 v0, 0x0

    .line 73
    .local v0, handled:Z
    iget-object v1, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    const/4 v2, 0x0

    aget-object v1, v1, v2

    invoke-static {p1, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_1

    .line 74
    invoke-direct {p0}, Lcom/android/calculator2/CalculatorEditText;->cutContent()V

    .line 75
    const/4 v0, 0x1

    .line 83
    :cond_0
    :goto_0
    return v0

    .line 76
    :cond_1
    iget-object v1, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    const/4 v2, 0x1

    aget-object v1, v1, v2

    invoke-static {p1, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_2

    .line 77
    invoke-direct {p0}, Lcom/android/calculator2/CalculatorEditText;->copyContent()V

    .line 78
    const/4 v0, 0x1

    goto :goto_0

    .line 79
    :cond_2
    iget-object v1, p0, Lcom/android/calculator2/CalculatorEditText;->mMenuItemsStrings:[Ljava/lang/String;

    const/4 v2, 0x2

    aget-object v1, v1, v2

    invoke-static {p1, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_0

    .line 80
    invoke-direct {p0}, Lcom/android/calculator2/CalculatorEditText;->pasteContent()V

    .line 81
    const/4 v0, 0x1

    goto :goto_0
.end method

.method public onTouchEvent(Landroid/view/MotionEvent;)Z
    .locals 2
    .parameter "event"

    .prologue
    .line 52
    invoke-virtual {p1}, Landroid/view/MotionEvent;->getActionMasked()I

    move-result v0

    const/4 v1, 0x1

    if-ne v0, v1, :cond_0

    .line 54
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->cancelLongPress()V

    .line 56
    :cond_0
    invoke-super {p0, p1}, Landroid/widget/EditText;->onTouchEvent(Landroid/view/MotionEvent;)Z

    move-result v0

    return v0
.end method

.method public performLongClick()Z
    .locals 1

    .prologue
    .line 61
    invoke-virtual {p0}, Lcom/android/calculator2/CalculatorEditText;->showContextMenu()Z

    .line 62
    const/4 v0, 0x1

    return v0
.end method
