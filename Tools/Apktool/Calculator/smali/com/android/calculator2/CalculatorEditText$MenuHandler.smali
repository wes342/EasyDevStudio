.class Lcom/android/calculator2/CalculatorEditText$MenuHandler;
.super Ljava/lang/Object;
.source "CalculatorEditText.java"

# interfaces
.implements Landroid/view/MenuItem$OnMenuItemClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/calculator2/CalculatorEditText;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "MenuHandler"
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/calculator2/CalculatorEditText;


# direct methods
.method private constructor <init>(Lcom/android/calculator2/CalculatorEditText;)V
    .locals 0
    .parameter

    .prologue
    .line 65
    iput-object p1, p0, Lcom/android/calculator2/CalculatorEditText$MenuHandler;->this$0:Lcom/android/calculator2/CalculatorEditText;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method synthetic constructor <init>(Lcom/android/calculator2/CalculatorEditText;Lcom/android/calculator2/CalculatorEditText$1;)V
    .locals 0
    .parameter "x0"
    .parameter "x1"

    .prologue
    .line 65
    invoke-direct {p0, p1}, Lcom/android/calculator2/CalculatorEditText$MenuHandler;-><init>(Lcom/android/calculator2/CalculatorEditText;)V

    return-void
.end method


# virtual methods
.method public onMenuItemClick(Landroid/view/MenuItem;)Z
    .locals 2
    .parameter "item"

    .prologue
    .line 67
    iget-object v0, p0, Lcom/android/calculator2/CalculatorEditText$MenuHandler;->this$0:Lcom/android/calculator2/CalculatorEditText;

    invoke-interface {p1}, Landroid/view/MenuItem;->getTitle()Ljava/lang/CharSequence;

    move-result-object v1

    invoke-virtual {v0, v1}, Lcom/android/calculator2/CalculatorEditText;->onTextContextMenuItem(Ljava/lang/CharSequence;)Z

    move-result v0

    return v0
.end method
